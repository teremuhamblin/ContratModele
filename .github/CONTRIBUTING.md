# 🤝 Contribuer à ContratModele (v1.0)

Merci de l'intérêt que vous portez à **ContratModele** ! Toutes les contributions visant à améliorer, moderniser ou enrichir ces modèles de contrats sont les bienvenues.

> ⚠️ **Rappel important :** Les contributions proposées sur ce dépôt sont partagées à titre purement informatif et communautaire. Elles ne constituent pas un conseil juridique personnalisé.

---

## 📌 Comment pouvez-vous contribuer ?

- **Corriger** des fautes d'orthographe, de mise en forme Markdown ou des renvois d'articles cassés ;
- **Actualiser** une clause suite à une évolution législative ou jurisprudentielle (Code civil, Code de commerce, Code du travail, CPI, RGPD, etc.) ;
- **Clarifier** des explications pédagogiques ou proposer des options alternatives (`Option A / Option B`) pour mieux équilibrer les intérêts entre Prestataire et Client ;
- **Proposer un nouveau modèle** dans `DOCS/` (ex : NDA / Accord de confidentialité, Contrat de cession de droits d'auteur, Contrat SaaS, Avenant de renouvellement, etc.) ;
- **Améliorer l'outillage** (ex : scripts d'export PDF via Pandoc, modèles CSS, automatisations GitHub Actions).

---

## 🛡️ Règles d'or avant toute contribution

Avant d'ouvrir une *Pull Request* (PR) portant sur un contrat dans `DOCS/`, merci de respecter impérativement ces 4 règles :

1. **Anonymisation totale (RGPD) :** Ne publiez **jamais** de données personnelles ou confidentielles réelles (noms de clients, SIRET, adresses postales, e-mails, tarifs réels confidentiels, signatures). Utilisez uniquement des champs génériques entre crochets `[Nom du Client]` ou `**XXXX**`.
2. **Origine licite des textes :** Ne copiez pas un contrat propriétaire appartenant à un client, une ESN ou un employeur sans autorisation. Soumettez uniquement des rédactions originales ou issues de sources publiques librement réutilisables (en citant la source si pertinent).
3. **Justification juridique :** Si vous modifiez ou ajoutez une clause de fond (délais de paiement, propriété intellectuelle, vigilance URSSAF, responsabilité...), précisez dans votre PR la **référence légale applicable** en droit français (ex : *art. L. 441-10 C. com.*, *art. 1218 C. civ.*).
4. **Transparence sur l'équilibre du contrat :** Indiquez clairement si une clause ajoutée protège plutôt le **Prestataire** ou le **Client**, ou proposez des variantes adaptées aux deux cas.

---

## ✍️ Conventions de rédaction Markdown (`DOCS/`)

Pour garantir un rendu propre sur GitHub et un export PDF sans défaut :

- Utilisez des titres hiérarchisés (`#`, `## Article X – ...`, `###`).
- Utilisez des **tableaux Markdown** pour les annexes, grilles tarifaires et blocs de signatures.
- **Évitez d'indenter les paragraphes avec 4 espaces** (en Markdown, cela transforme le texte en bloc de code illisible).
- Pour les modèles commentés (type `prestation-generique.md`), placez les explications dans des citations (`> 💡 **Explication :** ...`) afin de les distinguer visuellement du texte contractuel.
- Balisez clairement les valeurs à remplacer par `[...]` ou `**XXXX**`.

---

## 🔄 Processus de Pull Request (PR)

1. **Forkez** le dépôt sur votre compte GitHub.
2. Créez une branche dédiée depuis `main` :
   ```bash
   git checkout -b feat/ajout-modele-nda
   ```


Voici deux fichiers CONTRIBUTING.md et SECURITY.md spécialement conçus pour ContratModele v1.0.
Ils ne sont pas de simples copier-coller génériques : ils intègrent les enjeux spécifiques d'un dépôt de contrats juridiques (anonymisation stricte, respect du droit d'auteur, citation des lois françaises, double licence Apache-2.0 / CC-BY-4.0, et prévention des fuites de données personnelles sur les forks publics).
1. Fichier /CONTRIBUTING.md
Markdown
# 🤝 Contribuer à ContratModele (v1.0)

Merci de l'intérêt que vous portez à **ContratModele** ! Toutes les contributions visant à améliorer, moderniser ou enrichir ces modèles de contrats sont les bienvenues.

> ⚠️ **Rappel important :** Les contributions proposées sur ce dépôt sont partagées à titre purement informatif et communautaire. Elles ne constituent pas un conseil juridique personnalisé.

---

## 📌 Comment pouvez-vous contribuer ?

- **Corriger** des fautes d'orthographe, de mise en forme Markdown ou des renvois d'articles cassés ;
- **Actualiser** une clause suite à une évolution législative ou jurisprudentielle (Code civil, Code de commerce, Code du travail, CPI, RGPD, etc.) ;
- **Clarifier** des explications pédagogiques ou proposer des options alternatives (`Option A / Option B`) pour mieux équilibrer les intérêts entre Prestataire et Client ;
- **Proposer un nouveau modèle** dans `DOCS/` (ex : NDA / Accord de confidentialité, Contrat de cession de droits d'auteur, Contrat SaaS, Avenant de renouvellement, etc.) ;
- **Améliorer l'outillage** (ex : scripts d'export PDF via Pandoc, modèles CSS, automatisations GitHub Actions).

---

## 🛡️ Règles d'or avant toute contribution

Avant d'ouvrir une *Pull Request* (PR) portant sur un contrat dans `DOCS/`, merci de respecter impérativement ces 4 règles :

1. **Anonymisation totale (RGPD) :** Ne publiez **jamais** de données personnelles ou confidentielles réelles (noms de clients, SIRET, adresses postales, e-mails, tarifs réels confidentiels, signatures). Utilisez uniquement des champs génériques entre crochets `[Nom du Client]` ou `**XXXX**`.
2. **Origine licite des textes :** Ne copiez pas un contrat propriétaire appartenant à un client, une ESN ou un employeur sans autorisation. Soumettez uniquement des rédactions originales ou issues de sources publiques librement réutilisables (en citant la source si pertinent).
3. **Justification juridique :** Si vous modifiez ou ajoutez une clause de fond (délais de paiement, propriété intellectuelle, vigilance URSSAF, responsabilité...), précisez dans votre PR la **référence légale applicable** en droit français (ex : *art. L. 441-10 C. com.*, *art. 1218 C. civ.*).
4. **Transparence sur l'équilibre du contrat :** Indiquez clairement si une clause ajoutée protège plutôt le **Prestataire** ou le **Client**, ou proposez des variantes adaptées aux deux cas.

---

## ✍️ Conventions de rédaction Markdown (`DOCS/`)

Pour garantir un rendu propre sur GitHub et un export PDF sans défaut :

- Utilisez des titres hiérarchisés (`#`, `## Article X – ...`, `###`).
- Utilisez des **tableaux Markdown** pour les annexes, grilles tarifaires et blocs de signatures.
- **Évitez d'indenter les paragraphes avec 4 espaces** (en Markdown, cela transforme le texte en bloc de code illisible).
- Pour les modèles commentés (type `prestation-generique.md`), placez les explications dans des citations (`> 💡 **Explication :** ...`) afin de les distinguer visuellement du texte contractuel.
- Balisez clairement les valeurs à remplacer par `[...]` ou `**XXXX**`.

---

## 🔄 Processus de Pull Request (PR)

1. **Forkez** le dépôt sur votre compte GitHub.
2. Créez une branche dédiée depuis `main` :
   ```bash
   git checkout -b feat/ajout-modele-nda

3. Effectuez vos modifications en rédigeant des messages de commit clairs (*ex : docs: mise à jour article L. 8222-1, fix: correction renvoi article 5, feat: ajout modèle NDA)*.

4. Relisez le rendu Markdown directement sur GitHub pour vérifier l'absence de cassure de tableaux ou de mise en page.

5. Ouvrez une Pull Request vers main en décrivant :
l'objectif de la modification ;
les références légales ou sources utilisées le cas échéant.

### ⚖️ Licence de vos contributions
En soumettant une contribution à ContratModele, vous acceptez qu'elle soit distribuée selon le régime de double licence du projet :
- 》》 Dossier DOCS/ (modèles de contrats et guides) : licence CC BY 4.0 avec dispense d'attribution pour les contrats signés bilatéralement ;

- 》》 Reste du dépôt (racine, scripts, outillage) : licence Apache 2.0 (voir aussi NOTICE).

> Merci pour votre aide ! 🙌


