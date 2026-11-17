#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
Générateur interactif & batch de contrats pour ContratModele (v2.0).
- Détecte automatiquement les variables {{VARIABLE}} dans DOCS/
- Mémorise localement le profil Prestataire dans output/profil-prestataire.json
- Nettoie automatiquement les blocs pédagogiques (> 💡, > ⚠️, > **Note/Instructions...)
- Valide SIRET (Luhn) et délai légal LME (<= 60 jours)
- Exporte en Markdown et optionnellement en PDF via Pandoc (+ templates/style.tex)
"""

import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT_DIR / "DOCS"
OUTPUT_DIR = ROOT_DIR / "output"
TEMPLATES_DIR = ROOT_DIR / "templates"
PROFILE_FILE = OUTPUT_DIR / "profil-prestataire.json"

EXCLUDED_FILES = {"LICENSE.md", "README.md", "checklist-avant-signature.md"}
PLACEHOLDER_RE = re.compile(r"\{\{([A-Z0-9_]+)\}\}")
SAFE_NAME_RE = re.compile(r"^[a-zA-Z0-9_-]+$")
STRIP_BLOCK_START_RE = re.compile(
    r"^>\s*(?:⚠️\s*\*\*Avertissement|💡|\*\*(?:Instructions d'utilisation|Mode d'emploi|Note d'utilisation))"
)


def list_templates(docs_dir: Path = DOCS_DIR) -> list[Path]:
    if not docs_dir.is_dir():
        return []
    return sorted(p for p in docs_dir.glob("*.md") if p.name not in EXCLUDED_FILES)


def extract_placeholders(content: str) -> list[str]:
    return list(dict.fromkeys(PLACEHOLDER_RE.findall(content)))


def strip_pedagogical_blocks(content: str) -> str:
    """Supprime les avertissements repo, notes d'utilisation et encadrés > 💡 avant envoi client."""
    lines = content.splitlines()
    cleaned: list[str] = []
    seen_title = False
    i = 0

    while i < len(lines):
        line = lines[i]
        if STRIP_BLOCK_START_RE.match(line.lstrip()):
            while i < len(lines) and lines[i].lstrip().startswith(">"):
                i += 1
            while i < len(lines) and (
                not lines[i].strip() or (not seen_title and lines[i].strip() == "---")
            ):
                i += 1
            continue

        if line.lstrip().startswith("# "):
            seen_title = True
        cleaned.append(line)
        i += 1

    text = "\n".join(cleaned).strip() + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


def is_valid_luhn(digits: str) -> bool:
    total = 0
    reverse_digits = digits[::-1]
    for idx, ch in enumerate(reverse_digits):
        n = int(ch)
        if idx % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0


def validate_field(key: str, value: str) -> list[str]:
    """Retourne d'éventuels avertissements métier (non bloquants) sur une saisie."""
    warnings: list[str] = []
    if not value:
        return warnings

    if "SIRET" in key:
        compact = re.sub(r"\s+", "", value)
        if not compact.isdigit() or len(compact) != 14:
            warnings.append("Un SIRET français comporte exactement 14 chiffres.")
        elif not is_valid_luhn(compact):
            warnings.append("Ce SIRET ne passe pas la clé de contrôle Luhn (vérifiez la saisie).")

    if key == "DELAI_PAIEMENT_JOURS":
        try:
            days = int(value.strip())
            if days > 60:
                warnings.append("LME (art. L.441-10 C. com.) : le délai légal B2B est plafonné à 60 jours.")
        except ValueError:
            warnings.append("Un nombre entier de jours est attendu pour le délai de paiement.")

    return warnings


def is_profile_key(key: str) -> bool:
    return key.startswith("PRESTATAIRE_") or key in {"TRIBUNAL_COMPETENT", "VILLE_SIGNATURE"}


def load_profile(profile_path: Path = PROFILE_FILE) -> dict[str, str]:
    if not profile_path.is_file():
        return {}
    try:
        data = json.loads(profile_path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return {str(k): str(v) for k, v in data.items() if isinstance(v, str)}
    except (OSError, json.JSONDecodeError):
        pass
    return {}


def save_profile(profile: dict[str, str], profile_path: Path = PROFILE_FILE) -> None:
    profile_path.parent.mkdir(parents=True, exist_ok=True)
    profile_path.write_text(json.dumps(profile, ensure_ascii=False, indent=2), encoding="utf-8")


def render_template(content: str, values: dict[str, str], keep_notes: bool = False) -> str:
    rendered = content if keep_notes else strip_pedagogical_blocks(content)
    for key, val in values.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", val)
    return rendered


def sanitize_filename(name: str, fallback: str) -> str:
    cleaned = name.strip()
    if cleaned.endswith(".md"):
        cleaned = cleaned[:-3]
    if not cleaned or not SAFE_NAME_RE.match(cleaned):
        return fallback
    return cleaned


def export_pdf_with_pandoc(md_path: Path, pdf_path: Path) -> int:
    cmd = ["pandoc", str(md_path), "-o", str(pdf_path)]
    style_tex = TEMPLATES_DIR / "style.tex"
    if style_tex.is_file() and shutil.which("xelatex"):
        cmd.extend(["--pdf-engine=xelatex", "-H", str(style_tex)])
    res = subprocess.run(cmd, check=False)
    return res.returncode


def run_batch(args: argparse.Namespace) -> int:
    tpl_path = Path(args.template)
    if not tpl_path.is_file():
        tpl_path = DOCS_DIR / args.template
    if not tpl_path.is_file():
        print(f"[Erreur] Modèle introuvable : {args.template}")
        return 1

    vars_path = Path(args.vars)
    if not vars_path.is_file():
        print(f"[Erreur] Fichier JSON introuvable : {args.vars}")
        return 1

    raw_vars = json.loads(vars_path.read_text(encoding="utf-8"))
    values = {str(k): str(v) for k, v in raw_vars.items()}
    profile = load_profile()
    merged = {**profile, **values}

    content = tpl_path.read_text(encoding="utf-8")
    rendered = render_template(content, merged, keep_notes=args.keep_notes)

    remaining = extract_placeholders(rendered)
    if remaining:
        print(f"[Avertissement] {len(remaining)} variable(s) non remplie(s) : {', '.join(remaining)}")

    out_stem = sanitize_filename(args.out or "", f"{tpl_path.stem}-personnalise")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_md = OUTPUT_DIR / f"{out_stem}.md"
    out_md.write_text(rendered, encoding="utf-8")
    print(f"[OK] Contrat généré : {out_md.relative_to(ROOT_DIR)}")

    if args.pdf:
        if not shutil.which("pandoc"):
            print("[Erreur] Pandoc n'est pas installé pour l'export PDF.")
            return 1
        out_pdf = OUTPUT_DIR / f"{out_stem}.pdf"
        if export_pdf_with_pandoc(out_md, out_pdf) == 0:
            print(f"[OK] PDF généré : {out_pdf.relative_to(ROOT_DIR)}")
        else:
            print("[Avertissement] Échec de l'export PDF.")
    return 0


def run_interactive(keep_notes: bool = False) -> int:
    templates = list_templates()
    if not templates:
        print(f"[Erreur] Aucun modèle de contrat trouvé dans {DOCS_DIR}")
        return 1

    print("\n=== 📄 GÉNÉRATEUR DE CONTRAT — ContratModele v2.0 ===\n")
    for idx, tpl in enumerate(templates, start=1):
        print(f"  {idx:2d}. {tpl.name}")
    print("   0. Quitter\n")

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
    raw_content = template_path.read_text(encoding="utf-8")
    working_content = raw_content if keep_notes else strip_pedagogical_blocks(raw_content)
    placeholders = extract_placeholders(working_content)

    profile = load_profile()
    if profile:
        print(f"\n[Info] Profil Prestataire chargé ({len(profile)} champ(s) mémorisé(s)).")

    values: dict[str, str] = {}
    new_profile_entries: dict[str, str] = {}

    print(f"\nModèle sélectionné : {template_path.name}")
    if placeholders:
        print(f"{len(placeholders)} champ(s) à renseigner (Entrée = valeur mémorisée ou conserver {{{{...}}}}) :\n")
        for key in placeholders:
            label = key.replace("_", " ").capitalize()
            saved = profile.get(key, "")
            hint = f" [profil: {saved}]" if saved else ""
            val = input(f"  {label} ({{{{{key}}}}}){hint} : ").strip()

            final_val = val if val else saved
            if final_val:
                for warn in validate_field(key, final_val):
                    print(f"    ⚠️  {warn}")
                values[key] = final_val
                if is_profile_key(key) and final_val != saved:
                    new_profile_entries[key] = final_val

    rendered = render_template(raw_content, values, keep_notes=keep_notes)
    remaining = extract_placeholders(rendered)
    if remaining:
        print(f"\n[Avertissement] {len(remaining)} variable(s) non renseignée(s) : {', '.join(remaining)}")

    if new_profile_entries:
        save_ans = input("\nMémoriser les infos Prestataire pour les prochains contrats ? (o/N) : ").strip().lower()
        if save_ans in {"o", "oui", "y", "yes"}:
            save_profile({**profile, **new_profile_entries})
            print(f"[OK] Profil sauvegardé dans {PROFILE_FILE.relative_to(ROOT_DIR)}")

    default_out = f"{template_path.stem}-personnalise"
    raw_out = input(f"\nNom du fichier de sortie sans extension [{default_out}] : ")
    out_stem = sanitize_filename(raw_out, default_out)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_md = OUTPUT_DIR / f"{out_stem}.md"
    out_md.write_text(rendered, encoding="utf-8")
    print(f"\n[OK] Contrat généré : {out_md.relative_to(ROOT_DIR)}")

    if shutil.which("pandoc"):
        export_pdf = input("Exporter aussi en PDF via Pandoc ? (o/N) : ").strip().lower()
        if export_pdf in {"o", "oui", "y", "yes"}:
            out_pdf = OUTPUT_DIR / f"{out_stem}.pdf"
            if export_pdf_with_pandoc(out_md, out_pdf) == 0:
                print(f"[OK] PDF généré : {out_pdf.relative_to(ROOT_DIR)}")
            else:
                print("[Avertissement] Échec de l'export PDF (vérifiez votre moteur LaTeX/PDF).")
    else:
        print("[Astuce] Ouvrez index.html ou utilisez VS Code / Pandoc pour exporter ce .md en PDF.")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Générateur de contrats ContratModele")
    parser.add_argument("--template", help="Nom ou chemin du modèle dans DOCS/")
    parser.add_argument("--vars", help="Fichier JSON contenant les variables pour mode non-interactif")
    parser.add_argument("--out", help="Nom du fichier de sortie (sans extension)")
    parser.add_argument("--pdf", action="store_true", help="Exporter automatiquement en PDF via Pandoc")
    parser.add_argument("--keep-notes", action="store_true", help="Conserver les blocs pédagogiques > 💡")
    args = parser.parse_args()

    if args.template and args.vars:
        return run_batch(args)
    return run_interactive(keep_notes=args.keep_notes)


if __name__ == "__main__":
    sys.exit(main())
