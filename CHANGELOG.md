# Changelog

Toutes les évolutions notables de **ContratModele** sont documentées dans ce fichier.

## [v1.2.0] - 2026-11-17
### Ajouté
- 4 nouveaux modèles terrain : `avenant-prolongation.md`, `pv-recette.md`, `devis-cgv.md`, `mise-en-demeure-impaye.md`.
- `scripts/generate.py` v2.0 : mémorisation locale du profil Prestataire, nettoyage auto des blocs pédagogiques (`> 💡`, `> **Note...**`), validation SIRET (Luhn) & LME (60 j), mode batch `--vars`.
- Styles d'export PDF professionnels (`templates/style.tex`, `templates/contrat.css`).
- Application Web statique 100 % privée (`index.html`) compatible GitHub Pages.
- Tests unitaires (`tests/test_generate.py`) exécutés automatiquement par la CI.

## [v1.1.0]
### Ajouté
- Nouveaux modèles : `nda-confidentialite.md`, `prestation-forfait.md`, `cession-droits-pi.md`, `annexe-rgpd-dpa.md`, `checklist-avant-signature.md`.
- Standardisation complète de tous les modèles historiques au format `{{VARIABLE}}`.
- Générateur CLI initial `scripts/generate.py`, `.gitignore` et templates `.github/`.

## [v1.0.0]
### Ajouté
- Lancement initial des 5 modèles de contrats IT sous double licence Apache 2.0 + CC BY 4.0.
