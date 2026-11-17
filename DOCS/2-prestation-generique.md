> ⚠️ **Avertissement :** Modèle fourni à titre purement informatif (droit français). Il ne constitue pas un conseil juridique ; faites-le relire par un professionnel du droit avant signature.

> **Mode d'emploi de ce document (à supprimer avant envoi) :**
> Ce document est un **modèle pédagogique complet de contrat de prestation de services**.
> - Les blocs encadrés (`> 💡 ...`) vous expliquent **l'utilité, les risques et les options** de chaque clause : **ne les copiez pas dans votre contrat final**.
> - Conservez uniquement le texte des articles dont vous avez besoin, remplacez les champs `{{...}}` via `python3 scripts/generate.py` (ou manuellement) et ne gardez qu'une seule option lorsqu'un choix est proposé.

---

# Contrat de prestation de services

> 💡 **En-tête des Parties `[INDISPENSABLE]`**
> Identifiez précisément qui signe. Si vous exercez en **société** (SASU, EURL, SARL...), utilisez l'Option 1. Si vous êtes **Entrepreneur Individuel / Micro-entrepreneur**, utilisez l'Option 2.

**Entre les soussignés :**

*(Option 1 – Prestataire en société)*  
La société **{{PRESTATAIRE_NOM}}**, {{PRESTATAIRE_FORME_JURIDIQUE}} au capital de **{{PRESTATAIRE_CAPITAL_EUR}} €**, ayant son siège social au **{{PRESTATAIRE_ADRESSE}}**, immatriculée au RCS de **{{PRESTATAIRE_RCS_VILLE}}** sous le n° **{{PRESTATAIRE_SIREN}}**, représentée par **{{PRESTATAIRE_REPRESENTANT}}**, en qualité de **{{PRESTATAIRE_REPRESENTANT_FONCTION}}**,  

*(Option 2 – Prestataire en Entreprise Individuelle / Micro-entreprise)*  
**{{PRESTATAIRE_REPRESENTANT}}**, entrepreneur individuel exerçant sous le nom commercial **{{PRESTATAIRE_NOM}}**, domicilié(e) professionnellement au **{{PRESTATAIRE_ADRESSE}}**, immatriculé(e) sous le n° SIRET **{{PRESTATAIRE_SIRET}}**,  

*(ci-après dénommé(e) « **le Prestataire** »)*,

**d'une part,**

**Et**

La société **{{CLIENT_RAISON_SOCIALE}}**, {{CLIENT_FORME_JURIDIQUE}} au capital de **{{CLIENT_CAPITAL_EUR}} €**, ayant son siège social au **{{CLIENT_ADRESSE}}**, immatriculée au RCS de **{{CLIENT_RCS_VILLE}}** sous le n° **{{CLIENT_SIREN}}**, représentée par **{{CLIENT_REPRESENTANT}}**, en qualité de **{{CLIENT_REPRESENTANT_FONCTION}}**, dûment habilité(e),  
*(ci-après dénommée « **le Client** »)*,

**d'autre part.**

---

## Préambule

> 💡 **Explication `[FACULTATIF]`**
> Rappelez ici en quelques lignes le contexte du projet et les raisons qui motivent l'accord intervenu. En cas de litige futur sur l'interprétation d'une clause ambiguë, le juge s'appuiera sur ce préambule pour comprendre la commune intention des parties.

Il a été préalablement exposé que :  
**{{CONTEXTE_PREAMBULE}}** *(décrire en 3 à 5 lignes l'activité du Client, son besoin, et le contexte dans lequel le Prestataire est sollicité).*

Ceci exposé, il a été convenu ce qui suit :

---

## Article 1 – Objet

> 💡 **Explication `[INDISPENSABLE]`**
> Définissez aussi précisément que possible la prestation attendue (étude, audit, développement, expertise, accompagnement). Si la description technique est longue, renvoyez vers un cahier des charges en annexe afin d'éviter toute dérive de périmètre (*scope creep*).

Le présent contrat a pour objet la réalisation par le Prestataire de la mission de conseil et de prestation informatique suivante : **{{OBJET_MISSION}}** *(ou : la mission définie au cahier des charges figurant en Annexe du présent contrat et en faisant partie intégrante)*.

---

## Article 2 – Prix et modalités de paiement

> 💡 **Explication `[INDISPENSABLE]`**
> Deux modèles tarifaires principaux existent :
> 1. **Au forfait** : prix fixe pour un livrable et un calendrier déterminés (attention à bien verrouiller le cahier des charges).
> 2. **En régie (au temps passé / TJM)** : facturation à la journée si la durée ou le périmètre ne peut pas être figé à l'avance. Il est prudent d'indiquer un volume prévisionnel ou maximum de journées.
>
> **Attention légale :** Entre professionnels (art. L. 441-10 et D. 441-5 du Code de commerce), le délai de paiement ne peut pas dépasser 60 jours à compter de la date d'émission de la facture (ou 45 jours fin de mois), et **la mention des pénalités de retard et de l'indemnité forfaitaire de 40 € est obligatoire**.

**Option 1 – Prix forfaitaire :**  
En contrepartie de la réalisation des prestations définies à l'Article 1, le Client versera au Prestataire la somme forfaitaire de **{{MONTANT_FORFAIT_HT}} € HT**, majorée de la TVA en vigueur *(ou « TVA non applicable, art. 293 B du CGI »)*, ventilée de la manière suivante :
- **{{ACOMPTE_ECHEANCE_1}}** *(ex : 20 ou 30 % – Montant € HT)* à la signature des présentes ;
- **{{ACOMPTE_ECHEANCE_2}}** *(ex : 30 ou 40 % – Montant € HT)* à **{{JALON_ECHEANCE_2}}** *(ex : l'étape intermédiaire / J+X suivant la signature)* ;
- **{{SOLDE_ECHEANCE_3}}** *(ex : le solde – Montant € HT)* à la réception des livrables finaux.

*(Clause d'indexation optionnelle pour les contrats longs ou pluriannuels, utilisant par exemple l'indice Syntec :)*  
Les montants prévus seront révisés selon la formule : $P = P_0 \times \left(\frac{I}{I_0}\right)$, où $P$ est le prix révisé, $P_0$ le prix de base, $I$ le dernier indice **{{INDICE_REVISION}}** *(ex : Syntec)* publié à la date de révision, et $I_0$ l'indice connu à la date de prise d'effet du contrat.

**Option 2 – Prix en régie (à la journée) :**  
Les prestations définies à l'Article 1 seront facturées au Client sur la base d'un tarif journalier de **{{TJM_HT}} € HT par jour** *(majoré de la TVA en vigueur)*, pour un volume estimé de **{{JOURS_MAX}}** journées maximum *(modifiable par accord écrit des parties)*, facturé mensuellement sur la base d'un Compte Rendu d'Activité (CRA).  
*(Facultatif :)* Une rémunération variable de **{{REMUNERATION_VARIABLE_PCT}}** *(ex : X %)* assise sur **{{INDICATEUR_VARIABLE}}** *(indicateur objectif et quantifiable)* s'ajoutera en cas d'atteinte des objectifs convenus.

**Frais annexes (commun aux deux options) :**  
Les frais spécifiques engagés par le Prestataire (déplacement, hébergement, repas, licences ou achats dédiés) nécessaires à l'exécution de la prestation en dehors de son lieu d'exercice habituel seront facturés en sus au Client au réel, sur présentation de justificatifs et sous réserve de l'accord préalable et écrit du Client.

**Modalités de règlement et pénalités de retard (commun aux deux options) :**  
Les factures sont payables par virement bancaire dans un délai de **{{DELAI_PAIEMENT_JOURS}} jours** à compter de leur date d'émission. Conformément aux articles L. 441-10 et D. 441-5 du Code de commerce, tout retard de paiement entraîne de plein droit, sans rappel préalable, l'exigibilité de pénalités de retard calculées au taux d'intérêt appliqué par la Banque Centrale Européenne (BCE) à son opération de refinancement la plus récente majoré de 10 points de pourcentage (sans pouvoir être inférieur à 3 fois le taux d'intérêt légal), ainsi qu'une indemnité forfaitaire pour frais de recouvrement de **40 €** par facture impayée. À défaut de règlement huit (8) jours après mise en demeure restée sans effet, le Prestataire pourra suspendre ses prestations jusqu'au complet paiement.

---

## Article 3 – Durée

> 💡 **Explication `[INDISPENSABLE – à relier à l'Article 5]`**
> Au forfait, la durée correspond souvent au calendrier de livraison. En régie, fixez une date de fin ou un plafond de jours, avec possibilité de renouvellement par avenant écrit.

Le présent contrat prend effet le **{{DATE_DEBUT}}** et est conclu pour une durée de **{{DUREE_MISSION}}** *(ex : 6 mois)*, soit jusqu'au **{{DATE_FIN}}** *(ou jusqu'à la réception complète des livrables)*. Il pourra être prolongé ou renouvelé par accord écrit (avenant) entre les parties.

---

# Obligations du Prestataire

## Article 4 – Exécution de la prestation

> 💡 **Explication `[INDISPENSABLE]`**
> Précisez ici comment la mission est pilotée, si une équipe nominative est dédiée (et si son changement requiert l'accord du Client) et si un comité de pilotage est prévu. Rappelez aussi l'indépendance du Prestataire pour éviter tout risque de requalification en contrat de travail.

Le Prestataire s'engage à mener à bien la tâche précisée à l'Article 1, conformément aux règles de l'art, en toute indépendance dans l'organisation de ses moyens et sans lien de subordination vis-à-vis du Client.

À cet effet, il affecte les compétences *(ou l'équipe décrite en Annexe, dont toute modification substantielle nécessitera l'information ou l'accord préalable du Client)* nécessaires à la réalisation de la mission et remet, le cas échéant, une pré-étude au plus tard le **{{DATE_PRE_ETUDE}}**. Il sollicitera du Client tous les éléments nécessaires à la bonne menée de la mission, notamment dans le cadre des points de suivi ou du comité de pilotage convenus entre les parties.

---

## Article 5 – Calendrier et délais

> 💡 **Explication `[INDISPENSABLE]`**
> Un calendrier clair protège les deux parties. Attention toutefois : en tant que Prestataire, assurez-vous que les délais dépendent bien du respect par le Client de ses propres délais de fourniture d'accès et de validation !

Sous réserve du respect par le Client de ses obligations de collaboration et de validation dans les délais convenus, le calendrier prévisionnel est le suivant :
- La **Phase 1** définie au cahier des charges devra être achevée au plus tard le **{{DATE_PHASE_1}}** ;
- La **Phase 2**, assortie de la remise du pré-rapport / livrable intermédiaire, devra être achevée au plus tard le **{{DATE_PHASE_2}}** ;
- La **Phase 3** et les livrables finaux devront être délivrés au plus tard le **{{DATE_PHASE_3}}**.

Tout retard imputable au Client ou relevant de la force majeure entraîne automatiquement un décalage équivalent de ce calendrier.

---

## Article 6 – Nature des obligations

> 💡 **Explication `[FACULTATIF – mais très utile]`**
> La distinction **obligation de moyens** vs **obligation de résultat** détermine la charge de la preuve en cas de litige :
> - **Obligation de résultat** (typique du forfait sur un livrable technique précis) : si le résultat n'est pas livré conforme, le Prestataire est présumé responsable, sauf cause étrangère (faute du Client, force majeure).
> - **Obligation de moyens** (typique du conseil, de l'audit ou de la régie/AT) : le Client mécontent doit prouver que le Prestataire n'a pas mis en œuvre les diligences et compétences raisonnables attendues d'un professionnel.
> *(Note : la pertinence finale d'un conseil relève toujours d'une obligation de moyens, tandis que la remise physique d'un rapport à une date impérative peut relever d'une obligation de résultat).*

Pour l'accomplissement des diligences et prestations prévues à l'Article 1, le Prestataire s'engage à donner ses meilleurs soins, conformément aux règles de l'art. La présente obligation n'est, de convention expresse, qu'une **obligation de moyens** *(ou : une obligation de résultat quant à la conformité des livrables aux spécifications validées au cahier des charges)*.

---

## Article 7 – Obligation de confidentialité

> 💡 **Explication `[INDISPENSABLE]`**
> Il est important de protéger les informations sensibles échangées. Pensez à rendre cette clause **réciproque** (elle protège aussi vos propres méthodes et tarifs) et à fixer une durée après la fin du contrat.

Chacune des parties considérera comme strictement confidentiels, et s'interdit de divulguer à des tiers sans accord écrit préalable, toute information, document, donnée ou concept de nature technique, commerciale ou financière dont elle pourra avoir connaissance à l'occasion du présent contrat. Pour l'application de la présente clause, chaque partie se porte fort (article 1204 du Code civil) du respect de cette obligation par ses salariés et sous-traitants autorisés.

Toutefois, aucune partie ne saurait être tenue responsable d'une divulgation si les éléments en cause étaient déjà dans le domaine public à la date de la divulgation, étaient déjà licitement connus d'elle avant la signature du contrat, ont été obtenus de tiers par des moyens légitimes, ou doivent être communiqués en vertu d'une obligation légale. Cette obligation perdurera pendant **{{DUREE_CONFIDENTIALITE_ANS}} ans** *(ex : 5 ans)* après le terme du contrat.

---

# Obligations du Client

## Article 8 – Accès aux informations et locaux

> 💡 **Explication `[FACULTATIF]`**
> Utile si vous devez accéder aux serveurs, bases de données, codes sources ou locaux du Client pour accomplir votre mission.

Pour mener à bien la mission prise en charge, le Client accordera au Prestataire un accès contrôlé et sécurisé aux systèmes, locaux et catégories d'informations nécessaires à l'exécution des prestations, dans le respect des règles de sécurité notifiées par le Client.

---

## Article 9 – Obligation de collaboration

> 💡 **Explication `[FACULTATIF – vivement recommandé]`**
> Dans une mission de conseil ou d'IT, le Client ne peut pas rester passif : il doit vous fournir les accès, répondre à vos questions et désigner un interlocuteur décisionnaire. Sans cela, vous ne pouvez pas tenir vos délais.

Le Client tiendra à la disposition du Prestataire toutes les informations, accès et validations pouvant contribuer à la bonne réalisation de l'objet du présent contrat. À cette fin, le Client désigne un interlocuteur privilégié décisionnaire (**{{CLIENT_INTERLOCUTEUR_PROJET}}**) pour assurer le dialogue et le suivi dans les diverses étapes de la mission.

---

## Article 10 – Obligation de réception (recette)

> 💡 **Explication `[FACULTATIF – indispensable au forfait]`**
> La réception (recette) est l'acte par lequel le Client reconnaît que le livrable est conforme. Elle déclenche souvent le paiement du solde ou le passage à la phase suivante. **Astuce cruciale pour le Prestataire :** ajoutez toujours un délai au bout duquel le silence du Client vaut acceptation tacite, pour éviter qu'un Client ne bloque votre facture indéfiniment !

À la date prévue pour chaque jalon *(et notamment le **{{DATE_LIVRABLE_INTERMEDIAIRE}}** pour le pré-rapport ou livrable intermédiaire)*, le Prestataire remettra le livrable correspondant au Client, qui disposera d'un délai de **{{DELAI_RECETTE_JOURS}} jours ouvrés** pour formuler ses réserves motivées par écrit ou prononcer sa validation afin que la phase suivante puisse être engagée. À défaut de réserves écrites et motivées dans ce délai, le livrable sera réputé accepté sans réserve.

---

## Article 11 – Obligation de non-sollicitation de personnel

> 💡 **Explication `[FACULTATIF]`**
> Utile si vous intervenez avec une équipe ou des collaborateurs que vous ne voulez pas voir débauchés par le Client. Pour être valable devant les tribunaux français, cette clause doit être **proportionnée** dans le temps (12 à 24 mois maximum) et limitée aux collaborateurs ayant participé au projet (la limiter uniquement aux collaborateurs impliqués est plus sûr juridiquement que « tout collaborateur présent ou futur »).

Sauf accord écrit et préalable du Prestataire, le Client s'interdit d'engager ou de faire travailler directement ou indirectement tout collaborateur du Prestataire ayant participé à l'exécution du présent contrat, même si la sollicitation initiale émane dudit collaborateur. La présente clause produira ses effets pendant toute l'exécution du contrat et pendant **{{DUREE_NON_SOLLICITATION_MOIS}} mois** *(ex : 12 ou 24 mois)* à compter de sa cessation. En cas de non-respect, le Client versera au Prestataire une indemnité forfaitaire égale à **{{PENALITE_NON_SOLLICITATION_MOIS}} mois** de rémunération brute du collaborateur concerné, charges sociales patronales incluses.

---

# Jouissance des résultats et responsabilité

## Article 12 – Propriété des résultats et propriété intellectuelle

> 💡 **Explication `[INDISPENSABLE]`**
> Clause fondamentale en informatique, design ou rédaction !
> - **Si le résultat n'est pas une œuvre protégée** (simple conseil oral, recommandation stratégique non formalisée), il s'agit surtout d'en réserver l'usage.
> - **Si le résultat est une œuvre protégeable** (code source, maquette, documentation, étude détaillée), l'**article L. 131-3 du Code de la propriété intellectuelle (CPI)** exige de mentionner explicitement **chaque droit cédé** (reproduction, représentation, adaptation...), la **destination**, l'**étendue géographique** et la **durée**. Une formulation vague du type *"tous droits cédés"* est juridiquement invalide !
> - **Attention :** En vertu de l'**article L. 131-1 CPI**, la cession globale d'œuvres futures est interdite ; il faut rattacher la cession aux livrables précis du contrat, et surtout **conditionner le transfert au paiement intégral du prix**. Pensez aussi à protéger vos **outils préexistants** (scripts, bibliothèques maison).

**Option 1 – Étude / Conseil simple (sans création logicielle ou œuvre complexe) :**  
De convention expresse, **à compter du paiement intégral de la prestation**, les résultats de l'étude seront en la pleine maîtrise du Client qui pourra en disposer comme il l'entend pour ses besoins internes. Le Prestataire s'interdit de communiquer ou d'exploiter les résultats spécifiques réalisés exclusivement pour le Client, sauf autorisation écrite préalable de ce dernier.

**Option 2 – Développements informatiques, créations ou études protégeables (conforme L. 131-3 CPI) :**  
**Sous réserve du paiement intégral du prix des prestations correspondantes**, le Prestataire cède à titre exclusif au Client les droits patrimoniaux de propriété intellectuelle sur les livrables originaux conçus exclusivement pour le Client dans le cadre du présent contrat (codes sources spécifiques, documentations, créations graphiques).

Cette cession comprend :
- le droit de reproduction, de fixation et de duplication sur tout support numérique ou papier ;
- le droit de représentation, de diffusion et de commercialisation auprès de tout public ;
- le droit d'adaptation, de traduction, de modification, de correction et d'évolution (sous réserve du droit moral du Prestataire).

La présente cession est consentie pour les besoins d'exploitation du Client, pour le **monde entier** et pour toute la **durée légale de protection du droit d'auteur**. Le prix convenu à l'Article 2 inclut de façon forfaitaire le prix de cette cession (art. L. 131-4 CPI).

La présente cession ne porte pas sur les outils, méthodes, savoir-faire et briques logicielles développés antérieurement ou indépendamment par le Prestataire (*« Éléments Préexistants »*), ni sur les composants *open source* soumis à leurs licences propres. Sur ses Éléments Préexistants éventuellement intégrés aux livrables, le Prestataire concède au Client une licence d'utilisation non exclusive, mondiale et perpétuelle, strictement limitée à l'exploitation et à la maintenance des livrables.

---

## Article 13 – Garantie d'éviction

> 💡 **Explication `[FACULTATIF]`**
> Protège le Client contre le risque que vous lui livriez du code ou du contenu volé/contrefait appartenant à un tiers. Veillez à lier cette garantie au plafond de responsabilité de l'Article 14 pour éviter toute incohérence !

Dans les limites du plafond prévu à l'Article 14, le Prestataire garantit au Client qu'il dispose de tous les droits nécessaires sur les créations réalisées et le garantit contre toute revendication de tiers portant sur une prétendue contrefaçon des éléments fournis par le Prestataire au Client.

---

## Article 14 – Responsabilités

> 💡 **Explication `[FACULTATIF – mais fortement conseillé pour le Prestataire]`**
> En droit français, les clauses limitatives de responsabilité sont valables entre professionnels **sauf** en cas de faute lourde, de dol (faute intentionnelle), de dommage corporel, ou si la clause vide de sa substance l'**obligation essentielle** du contrat (**article 1170 du Code civil**). Il est donc plus sûr juridiquement de **plafonner** votre responsabilité au montant du contrat (et d'exclure les dommages indirects) plutôt que d'essayer de supprimer toute responsabilité.

La responsabilité éventuelle du Prestataire ne peut être engagée qu'en cas de faute prouvée lui étant directement imputable. En aucun cas, le Prestataire n'encourra de responsabilité au titre des dommages indirects (perte de bénéfices, perte de chiffre d'affaires, perte de données, trouble commercial ou atteinte à l'image).

En tout état de cause (sauf faute lourde ou dolosive), quels que soient le fondement de la réclamation et la procédure suivie, la responsabilité totale et cumulée du Prestataire au titre du présent contrat sera limitée à un montant n'excédant pas la somme totale HT effectivement payée par le Client au titre des présentes *(ou au cours des 12 derniers mois)*.

---

## Article 15 – Pénalités de retard

> 💡 **Explication `[FACULTATIF]`**
> Le Client peut demander des pénalités en cas de retard de livraison. Si vous les acceptez en tant que Prestataire, exigez deux garde-fous : qu'elles ne s'appliquent **que si le retard vient exclusivement de vous**, et qu'elles soient **plafonnées** (par exemple à 5 % ou 10 % du prix total).

Tout dépassement des délais impératifs stipulés à l'Article 5 exclusivement imputable au Prestataire *(à l'exclusion de tout retard du Client ou cas de force majeure)* entraînera, après mise en demeure restée infructueuse pendant huit (8) jours, l'application d'une pénalité de **{{PENALITE_RETARD_JOURNALIERE}}** *(ex : 0,5 % du montant HT de la phase en retard)* par jour calendaire de retard, dans la limite d'un **plafond cumulé de {{PLAFOND_PENALITES_RETARD_PCT}} %** *(ex : 5 ou 10)* du montant total HT du contrat.

---

# Fin du contrat et sous-traitance

## Article 16 – Résolution pour manquement (clause résolutoire)

> 💡 **Explication `[INDISPENSABLE]`**
> Prévue par les **articles 1224 et 1225 du Code civil** (qui ont remplacé l'ancien article 1184 depuis la réforme de 2016), cette clause permet de mettre fin au contrat automatiquement sans passer d'abord devant le juge, en cas de faute grave non réparée après mise en demeure. Mentionnez précisément les obligations essentielles concernées pour éviter les abus.

Tout manquement grave de l'une ou l'autre des parties aux obligations essentielles qu'elle a en charge — et notamment au paiement du prix (Article 2), aux délais impératifs (Article 5), à la confidentialité (Article 7), à la collaboration (Article 9) ou à la propriété intellectuelle (Article 12) — entraînera, si bon semble au créancier de l'obligation inexécutée, la résolution de plein droit du présent contrat, **quinze (15) jours** après mise en demeure d'exécuter par lettre recommandée avec accusé de réception (LRAR) visant expressément la présente clause résolutoire et demeurée sans effet, sans préjudice de tous dommages et intérêts éventuels.

---

## Article 17 – Résiliation hors faute (pour convenance)

> 💡 **Explication `[FACULTATIF]`**
> Utile dans un contrat en régie / à durée indéterminée pour permettre à chaque partie de sortir proprement moyennant un préavis. En revanche, dans un contrat au **forfait** avec un objectif ferme, ne l'ajoutez pas (ou prévoyez une indemnité de dédit pour couvrir le travail déjà engagé).

**Option 1 – Résiliation avec préavis (adapté à la régie / mission continue) :**  
Le présent contrat pourra être résilié à tout moment par chacune des parties, sous réserve d'un préavis écrit de **{{PREAVIS_RESILIATION_JOURS}} jours** *(ex : 21 ou 30 jours)*. Dans cette hypothèse, les sommes correspondant aux prestations déjà réalisées jusqu'à la fin du préavis demeureront acquises au Prestataire et le Client pourra faire usage des livrables déjà remis et payés.

**Option 2 – Départ d'un intervenant clé :**  
Dans le cas où **{{INTERVENANT_CLE_NOM}}** viendrait à être dans l'impossibilité définitive d'exécuter la mission sans faute du Prestataire, les parties se rapprocheront pour convenir d'un remplacement ; à défaut d'accord, le contrat pourra être résilié avec un préavis d'un (1) mois, les phases ou jours réalisés restant dus.

---

## Article 18 – Sous-traitance

> 💡 **Explication `[FACULTATIF]`**
> Choisissez l'option adaptée à votre situation (ne gardez qu'une seule option !).

- **Option A (Sous-traitance autorisée pour un tiers identifié) :** Les tâches précisées à l'Article 1 concernant **{{PHASES_SOUS_TRAITEES}}** pourront être exécutées par la société **{{SOUS_TRAITANT_NOM}}**, en qualité de sous-traitant, ce que reconnaît et accepte le Client. Le Prestataire demeure seul responsable envers le Client de la bonne exécution des prestations sous-traitées.
- **Option B (Sous-traitance soumise à accord) :** Le Prestataire ne pourra sous-traiter tout ou partie des prestations définies à l'Article 1 qu'avec l'accord préalable et écrit du Client, et demeurera en tout état de cause pleinement responsable de leur exécution.
- **Option C (Sous-traitance interdite) :** Le présent contrat étant conclu en considération des compétences propres du Prestataire, celui-ci s'interdit de sous-traiter à quiconque la réalisation des travaux définis à l'Article 1.

---

## Article 19 – Cession de contrat

> 💡 **Explication `[FACULTATIF]`**
> Interdit à une partie de transférer le contrat lui-même à une autre entreprise sans l'accord de l'autre partie.

Le présent contrat est conclu *intuitu personae*. Sauf accord préalable et écrit de l'autre partie, aucune des parties ne pourra céder ou transférer à un tiers tout ou partie de ses droits et obligations au titre du présent contrat.

---

## Article 20 – Référencement commercial

> 💡 **Explication `[FACULTATIF]`**
> Permet au Prestataire de mentionner le Client dans son portfolio ou sur son site web. Si le Client refuse, remplacez par une interdiction sauf accord écrit.

Le Client autorise le Prestataire à faire figurer le nom et le logo du Client parmi ses références commerciales pour présenter les travaux accomplis dans le cadre du présent contrat *(sauf opposition écrite du Client ou divulgation d'informations confidentielles)*.

---

# Clauses générales, conformité et litiges

## Article 21 – Intégralité et interprétation du contrat

> 💡 **Explication `[FACULTATIF]`**
> Appelée « clause des quatre coins » (*entire agreement*), elle évite qu'un e-mail commercial ancien ne soit utilisé pour contredire le contrat final signé. Notez que la réforme du Code civil de 2016 a déplacé les règles d'interprétation aux **articles 1188 et suivants du Code civil** (qui remplacent les anciens articles 1156 et suivants).

Le présent contrat et ses annexes expriment l'intégralité des engagements des parties. Toutes correspondances, offres ou propositions antérieures à sa signature sont considérées comme non avenues. Toute modification devra faire l'objet d'un avenant écrit signé par les deux parties.

---

## Article 22 – Force majeure et imprévision

> 💡 **Explication `[FACULTATIF – recommandé]`**
> Protège les parties en cas d'événement imprévisible et irrésistible empêchant l'exécution (**article 1218 du Code civil**).

Conformément à l'article 1218 du Code civil, aucune des parties ne sera tenue responsable d'un retard ou d'une inexécution résultant d'un cas de force majeure. L'exécution des obligations est suspendue pendant la durée de l'événement ; si l'empêchement perdure au-delà de trente (30) jours, chaque partie pourra résilier le contrat de plein droit par notification écrite, sans indemnité.

---

## Article 23 – Obligation de vigilance sociale

> 💡 **Explication `[INDISPENSABLE si le contrat atteint ou dépasse 5 000 € HT]`**
> Aux termes des **articles L. 8222-1 et D. 8222-5 du Code du travail**, tout client professionnel doit vérifier que son prestataire est à jour de ses cotisations sociales pour tout contrat d'un montant global d'au moins 5 000 € HT.

Pour tout contrat d'un montant global au moins égal à 5 000 € HT, le Prestataire remettra au Client, à la signature puis tous les six (6) mois jusqu'au terme du contrat : une attestation de vigilance URSSAF de moins de six (6) mois et un justificatif d'immatriculation à jour (extrait Kbis, avis SIRENE ou extrait RNE).

---

## Article 24 – Données à caractère personnel (RGPD)

> 💡 **Explication `[INDISPENSABLE dès lors que vous traitez des données de personnes]`**
> Chaque partie doit respecter le **RGPD (UE 2016/679)**. Si le Prestataire accède à des bases de données contenant des données personnelles (clients, salariés, utilisateurs du Client) pour le compte du Client, il agit en tant que **sous-traitant** au sens de l'article 28 du RGPD et un accord de sous-traitance (DPA) devra être annexé.

Chaque partie s'engage à respecter la réglementation applicable aux données à caractère personnel (Loi Informatique et Libertés modifiée et RGPD). Les coordonnées professionnelles des signataires et interlocuteurs ne sont traitées que pour la gestion du contrat. Si le Prestataire traite des données personnelles pour le compte du Client dans le cadre de la mission, les parties concluront un accord de sous-traitance conforme à l'article 28 du RGPD.

---

## Article 25 – Médiation

> 💡 **Explication `[FACULTATIF]`**
> Permet de tenter une solution amiable encadrée avant de saisir un tribunal.

En cas de différend relatif au présent contrat, les parties s'engagent à rechercher une solution amiable, le cas échéant avec l'aide d'un médiateur désigné d'un commun accord, dans un délai de trente (30) jours suivant la notification écrite du litige. Les frais de médiation seront supportés par moitié par chacune des parties.

---

## Article 26 – Loi applicable et juridiction compétente

> 💡 **Explication `[INDISPENSABLE]`**
> - **Loi applicable :** Indispensable surtout si l'un des partenaires est basé à l'étranger.
> - **Tribunal compétent :** Attention ! En vertu de l'**article 48 du Code de procédure civile**, une clause désignant à l'avance un tribunal géographique spécifique n'est valable **que si les deux parties ont la qualité de commerçant** (ex : SAS, SARL, EURL). Si vous êtes entrepreneur individuel / profession libérale non-commerçant, les règles légales de compétence s'appliquent à défaut d'accord.

Le présent contrat est soumis au **droit français**.

À défaut d'accord amiable dans les conditions de l'Article 25, tout litige susceptible de s'élever entre les parties à propos de la formation, de l'exécution, de l'interprétation ou de la résiliation du présent contrat sera de la compétence exclusive du **Tribunal de commerce de {{TRIBUNAL_COMPETENT}}** *(entre sociétés commerciales)*.

---

## Article 27 – Arbitrage *(Alternative à l'Article 26)*

> 💡 **Explication `[FACULTATIF – déconseillé pour les petits/moyens contrats]`**
> L'arbitrage offre confidentialité et rapidité pour des litiges industriels complexes, mais il coûte **très cher** (honoraires des arbitres et frais administratifs à la charge des parties). Pour une mission de freelance ou de PME, préférez l'Article 26 (Tribunal de commerce). Notez que depuis 2016 (art. 2061 C. civ.), l'arbitrage est ouvert aux contrats conclus à raison d'une activité professionnelle, et est régi par les articles 1442 et suivants du **Code de procédure civile** (et non plus « nouveau » code de procédure civile).

*(Clause à n'utiliser qu'en remplacement de l'Article 26 si vous optez pour l'arbitrage :)*  
Tout litige susceptible de s'élever entre les parties sera tranché conformément au règlement de conciliation et d'arbitrage de **{{INSTITUTION_ARBITRALE}}**.

---

## Article 28 – Signature électronique

> 💡 **Explication `[FACULTATIF – pratique]`**
> Confirme la validité d'une signature via DocuSign, Yousign, Universign, etc. (articles 1366 et 1367 du Code civil).

Les parties conviennent que le présent contrat pourra être signé par voie électronique conformément aux articles 1366 et 1367 du Code civil, ce procédé ayant la même force probante qu'une signature manuscrite.

---

Fait à **{{VILLE_SIGNATURE}}**, le **{{DATE_SIGNATURE}}**, en deux (2) exemplaires originaux *(ou signé électroniquement)*.

| Pour le **Client** ({{CLIENT_RAISON_SOCIALE}}) | Pour le **Prestataire** ({{PRESTATAIRE_NOM}}) |
| :--- | :--- |
| *Nom et qualité :* {{CLIENT_REPRESENTANT}} — {{CLIENT_REPRESENTANT_FONCTION}} | *Nom et qualité :* {{PRESTATAIRE_REPRESENTANT}} — {{PRESTATAIRE_REPRESENTANT_FONCTION}} |
| *Signature :* | *Signature :* |
