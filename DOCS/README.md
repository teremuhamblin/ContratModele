# 📚 Index des modèles & Dictionnaire des variables (`DOCS/`)

Tous les contrats ci-dessous sont rédigés pour le **droit français**, sous licence **[CC BY 4.0](LICENSE.md)** (avec dispense d'attribution pour vos contrats signés), et utilisent la syntaxe `{{VARIABLE}}` pour `scripts/generate.py`.

## Modèles disponibles

* **Contrats principaux :** `assistance-technique-freelance.md`, `prestation-generique.md`, `prestation-forfait.md`, `assistance-technique.md`, `contrat-service.md`, `maintenance-informatique.md`, `devis-cgv.md`
* **Avenants, clôture & recouvrement :** `avenant-prolongation.md`, `pv-recette.md`, `mise-en-demeure-impaye.md`
* **Confidentialité, PI & RGPD :** `nda-confidentialite.md`, `cession-droits-pi.md`, `annexe-rgpd-dpa.md`
* **Guide de relecture :** `checklist-avant-signature.md`

## Variables standardisées recommandées (pour nouveaux modèles)

* **Prestataire :** `{{PRESTATAIRE_NOM}}`, `{{PRESTATAIRE_FORME_JURIDIQUE}}`, `{{PRESTATAIRE_SIRET}}`, `{{PRESTATAIRE_ADRESSE}}`, `{{PRESTATAIRE_REPRESENTANT}}`, `{{PRESTATAIRE_REPRESENTANT_FONCTION}}`, `{{PRESTATAIRE_EMAIL}}`
* **Client :** `{{CLIENT_RAISON_SOCIALE}}`, `{{CLIENT_FORME_JURIDIQUE}}`, `{{CLIENT_SIRET}}`, `{{CLIENT_ADRESSE}}`, `{{CLIENT_REPRESENTANT}}`, `{{CLIENT_REPRESENTANT_FONCTION}}`
* **Mission & Tarifs :** `{{OBJET_MISSION}}`, `{{DATE_DEBUT}}`, `{{DATE_FIN}}`, `{{TJM_HT}}`, `{{MONTANT_FORFAIT_HT}}`, `{{DELAI_PAIEMENT_JOURS}}`
* **Signature & Juridiction :** `{{VILLE_SIGNATURE}}`, `{{DATE_SIGNATURE}}`, `{{TRIBUNAL_COMPETENT}}`
