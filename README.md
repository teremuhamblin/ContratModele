<div align="center">

# 📄 ContratModele
### Modèles de contrats informatiques pour freelances, consultants & développeurs (Droit FR)

Une bibliothèque ouverte de contrats au format **Markdown**, faciles à lire, personnaliser et exporter en **PDF**.

![Version](https://img.shields.io/badge/Version-v1.1.0-16A34A?style=for-the-badge&logo=semanticrelease&logoColor=white&labelColor=1E293B)
![Juridiction](https://img.shields.io/badge/Droit-Fran%C3%A7ais%20%7C%20RGPD-2563EB?style=for-the-badge&logo=scales&logoColor=white&labelColor=1E293B)
![Modèles](https://img.shields.io/badge/Mod%C3%A8les-9%20Documents-16A34A?style=for-the-badge&logo=markdown&logoColor=white&labelColor=1E293B)
![Licences](https://img.shields.io/badge/Licences-Apache%202.0%20%2B%20CC%20BY%204.0-F59E0B?style=for-the-badge&logo=creativecommons&logoColor=white&labelColor=1E293B)

[⭐ Modèle recommandé](#-le-modèle-recommandé-pour-les-indépendants) • [📚 Tous les modèles](#-catalogue-des-modèles) • [⚙️ Générateur](#-comment-utiliser-ces-modèles-) • [✅ Check-list](DOCS/checklist-avant-signature.md) • [⚖️ Licences](#️-licences)

</div>

---

> [!NOTE]
> **Périmètre juridique :** Les modèles de ce dépôt sont rédigés pour le **droit français** (EI, EURL, SASU, SAS, SARL — mentions SIRET, LME et RGPD). Si vous exercez dans un autre pays, adaptez les clauses de juridiction et les mentions légales obligatoires.

---

## ⭐ Le modèle recommandé pour les indépendants

Si vous êtes freelance et démarrez une mission chez un client (en direct ou via un intermédiaire), le modèle le plus adapté à votre situation est :

👉 **[`DOCS/assistance-technique-freelance.md`](DOCS/assistance-technique-freelance.md)**

---

## 📚 Catalogue des modèles

### Contrats principaux

| Modèle | Type / Cas d'usage | Quand le choisir ? |
| :--- | :--- | :--- |
| **[`assistance-technique-freelance.md`](DOCS/assistance-technique-freelance.md)** | ⭐ Freelance IT | Mission en régie en tant qu'indépendant (recommandé) |
| **[`prestation-generique.md`](DOCS/prestation-generique.md)** | Prestation de service | Modèle polyvalent avec explications détaillées par clause |
| **[`prestation-forfait.md`](DOCS/prestation-forfait.md)** | Forfait / Projet clé en main | Développement avec cahier des charges, jalons et PV de recette |
| **[`assistance-technique.md`](DOCS/assistance-technique.md)** | Assistance Technique (AT) | Régie informatique classique |
| **[`contrat-service.md`](DOCS/contrat-service.md)** | B2B / Entreprises | Contrat de prestation entre deux sociétés (ex. sous-traitance ESN) |
| **[`maintenance-informatique.md`](DOCS/maintenance-informatique.md)** | TMA & AT | Tierce Maintenance Applicative et support récurrent |

### Clauses, annexes & sécurité juridique

| Document | Rôle | Usage |
| :--- | :--- | :--- |
| **[`nda-confidentialite.md`](DOCS/nda-confidentialite.md)** | Accord de confidentialité (NDA) | À faire signer avant un audit, un chiffrage ou un partage de code |
| **[`cession-droits-pi.md`](DOCS/cession-droits-pi.md)** | Cession de droits (PI) | Encadrer la cession du code source (*Foreground* vs *Background IP*) |
| **[`annexe-rgpd-dpa.md`](DOCS/annexe-rgpd-dpa.md)** | Annexe RGPD (DPA) | Obligatoire dès l'accès à des données personnelles en production |
| **[`checklist-avant-signature.md`](DOCS/checklist-avant-signature.md)** | ✅ Check-list de relecture | Les points critiques à vérifier avant de signer |

---

## 🛠️ Comment utiliser ces modèles ?

### Option A — Méthode rapide (automatisée avec Python 3)

Le script `scripts/generate.py` détecte automatiquement les champs `{{VARIABLE}}` d'un modèle, vous les demande en console et génère le contrat prêt dans `output/` (ignoré par Git) :

```bash
python3 scripts/generate.py
```

### Option B — Méthode manuelle & Export PDF

1. Ouvrez le fichier souhaité dans `DOCS/` et copiez son contenu (ou clonez le dépôt).
2. Remplacez tous les champs `{{VARIABLE}}` (sociétés, SIRET, TJM/forfait, dates, périmètre).
3. Relisez chaque clause à l'aide de la **[check-list avant signature](DOCS/checklist-avant-signature.md)**.
4. Exportez le document final en **PDF** (via VS Code *Markdown PDF*, Typora ou **Pandoc**) :
   ```bash
   pandoc DOCS/assistance-technique-freelance.md -o contrat.pdf --pdf-engine=xelatex -V geometry:margin=2cm
   ```

---

## ⚠️ Avertissement juridique

> [!WARNING]
> Les modèles présents dans ce dépôt sont fournis **à titre purement informatif**. Ils ne constituent en aucun cas un conseil juridique. La législation évoluant régulièrement (RGPD, propriété intellectuelle, droit du travail / requalification), faites relire vos contrats par un professionnel du droit (avocat ou juriste) avant toute signature.

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! Consultez les modèles d'*Issue* et de *Pull Request* pour :
* Corriger une coquille ou clarifier une clause ;
* Mettre à jour un modèle suite à une évolution légale ;
* Proposer un nouveau modèle utile à la communauté (en utilisant les variables standardisées `{{NOM_CHAMP}}`).

---

## ⚖️ Licences

- **Projet global (structure, scripts `scripts/`, outillage)** : distribué sous licence **[Apache 2.0](LICENSE)** (voir également [`NOTICE`](NOTICE)).
- **Modèles de contrats (`DOCS/`)** : distribués sous licence **[CC BY 4.0](DOCS/LICENSE.md)** avec **dispense d'attribution pour vos contrats signés** (vous pouvez les adapter et les utiliser commercialement avec vos clients sans mentionner `ContratModele`).
