#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
Générateur interactif de contrats pour ContratModele.
Détecte automatiquement les placeholders {{VARIABLE}} dans DOCS/ et génère
un document personnalisé dans output/ (avec export PDF optionnel via Pandoc).
"""

from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT_DIR / "DOCS"
OUTPUT_DIR = ROOT_DIR / "output"

EXCLUDED_FILES = {"LICENSE.md", "README.md", "checklist-avant-signature.md"}
PLACEHOLDER_RE = re.compile(r"\{\{([A-Z0-9_]+)\}\}")
SAFE_NAME_RE = re.compile(r"^[a-zA-Z0-9_-]+$")


def list_templates() -> list[Path]:
    if not DOCS_DIR.is_dir():
        return []
    return sorted(
        p for p in DOCS_DIR.glob("*.md")
        if p.name not in EXCLUDED_FILES
    )


def extract_placeholders(content: str) -> list[str]:
    # Préserve l'ordre d'apparition sans doublon
    return list(dict.fromkeys(PLACEHOLDER_RE.findall(content)))


def sanitize_filename(name: str, fallback: str) -> str:
    cleaned = name.strip().removesuffix(".md")
    if not cleaned or not SAFE_NAME_RE.match(cleaned):
        return fallback
    return cleaned


def main() -> int:
    templates = list_templates()
    if not templates:
        print(f"[Erreur] Aucun modèle de contrat trouvé dans {DOCS_DIR}")
        return 1

    print("\n=== 📄 GÉNÉRATEUR DE CONTRAT — ContratModele ===\n")
    for idx, tpl in enumerate(templates, start=1):
        print(f"  {idx}. {tpl.name}")
    print("  0. Quitter\n")

    raw_choice = input("Choisissez un modèle (numéro) : ").strip()
    if raw_choice == "0" or not raw_choice:
        print("Annulé.")
        return 0

    try:
        choice = int(raw_choice)
        if not (1 <= choice <= len(templates)):
            raise ValueError
    except ValueError:
        print("[Erreur] Choix invalide.")
        return 1

    template_path = templates[choice - 1]
    content = template_path.read_text(encoding="utf-8")
    placeholders = extract_placeholders(content)

    print(f"\nModèle sélectionné : {template_path.name}")
    if not placeholders:
        print("[Info] Aucune variable {{...}} détectée dans ce fichier.")
        print("       (Uniformisez les champs avec {{NOM_CHAMP}} pour automatiser ce modèle.)")
    else:
        print(f"{len(placeholders)} champ(s) à renseigner (Entrée pour laisser {{...}}) :\n")
        values: dict[str, str] = {}
        for key in placeholders:
            label = key.replace("_", " ").capitalize()
            val = input(f"  {label} ({{{{{key}}}}}) : ").strip()
            if val:
                values[key] = val

        for key, val in values.items():
            content = content.replace(f"{{{{{key}}}}}", val)

    default_out = f"{template_path.stem}-personnalise"
    raw_out = input(f"\nNom du fichier de sortie sans extension [{default_out}] : ")
    out_stem = sanitize_filename(raw_out, default_out)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_md = OUTPUT_DIR / f"{out_stem}.md"
    out_md.write_text(content, encoding="utf-8")
    print(f"\n[OK] Contrat généré : {out_md.relative_to(ROOT_DIR)}")

    if shutil.which("pandoc"):
        export_pdf = input("Exporter aussi en PDF via Pandoc ? (o/N) : ").strip().lower()
        if export_pdf in {"o", "oui", "y", "yes"}:
            out_pdf = OUTPUT_DIR / f"{out_stem}.pdf"
            res = subprocess.run(
                ["pandoc", str(out_md), "-o", str(out_pdf)],
                check=False,
            )
            if res.returncode == 0:
                print(f"[OK] PDF généré : {out_pdf.relative_to(ROOT_DIR)}")
            else:
                print("[Avertissement] Échec de l'export PDF (vérifiez votre moteur LaTeX/PDF).")
    else:
        print("[Astuce] Installez Pandoc ou utilisez VS Code pour exporter ce .md en PDF.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
