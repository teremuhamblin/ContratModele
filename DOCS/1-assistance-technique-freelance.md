> ⚠️ **Avertissement :** Modèle fourni à titre purement informatif (droit français). Il ne constitue pas un conseil juridique ; faites-le relire par un professionnel du droit avant signature.

> **Instructions d'utilisation (à supprimer avant envoi) :**
> - Contrat adapté à un **Freelance en Assistance Technique (A.T.)** facturé à la journée (régie).
> - Basé sur [assistance-technique.md](assistance-technique.md).
> - Utilisez `python3 scripts/generate.py` ou remplacez chaque variable `{{...}}` par les valeurs négociées avec le CLIENT.

---

# Contrat de prestation d'assistance technique

**Entre les soussignés :**

La société **{{CLIENT_RAISON_SOCIALE}}**, {{CLIENT_FORME_JURIDIQUE}} au capital de **{{CLIENT_CAPITAL_EUR}} €**, dont le siège social est situé au **{{CLIENT_ADRESSE}}**, immatriculée au Registre du Commerce et des Sociétés de **{{CLIENT_RCS_VILLE}}** sous le numéro **{{CLIENT_SIREN}}**, représentée par **{{CLIENT_REPRESENTANT}}**, en qualité de **{{CLIENT_REPRESENTANT_FONCTION}}**, dûment habilité(e) aux fins des présentes,  
*(ci-après désignée « **le CLIENT** »)*,

**d'une part, et**

**{{PRESTATAIRE_NOM}}**, {{PRESTATAIRE_FORME_JURIDIQUE}}, dont le siège social / domicile professionnel est situé au **{{PRESTATAIRE_ADRESSE}}**, immatriculé(e) sous le numéro SIRET **{{PRESTATAIRE_SIRET}}** *(immatriculation complémentaire RCS/RNE le cas échéant : {{PRESTATAIRE_IMMATRICULATION_COMPLEMENT}})*, représenté(e) par **{{PRESTATAIRE_REPRESENTANT}}**, en qualité de **{{PRESTATAIRE_REPRESENTANT_FONCTION}}**,  
*(ci-après désigné(e) « **le PRESTATAIRE** »)*,

**d'autre part,**

*(ci-après désignés ensemble « **les Parties** » et individuellement « **une Partie** »)*.

**Il a été convenu ce qui suit :**

---

## Article 1 – Objet et nature de la mission

Le présent contrat a pour objet la réalisation par le PRESTATAIRE d'une mission d'assistance technique informatique pour le compte du CLIENT, portant sur : **{{OBJET_MISSION}}**.

Les obligations du PRESTATAIRE consistent à faire bénéficier le CLIENT de sa compétence et de son savoir-faire technique dans le cadre des projets informatiques de ce dernier. À ce titre, le PRESTATAIRE est soumis à une **obligation de moyens**.

Le CLIENT assure seul la direction, le pilotage et la maîtrise d'œuvre des projets et demeure, à ce titre, seul responsable des résultats finaux de ceux-ci.

Le CLIENT s'engage à apporter sa pleine collaboration au PRESTATAIRE afin de permettre la bonne exécution de la mission, et notamment à :
- fournir au PRESTATAIRE les informations, accès et documentations indispensables à la compréhension des besoins ;
- mettre à la disposition du PRESTATAIRE les moyens techniques ou matériels nécessaires si la mission l'exige.

Le présent contrat est exclusif de toute mise à disposition de personnel entrant dans le cadre du travail temporaire ou du prêt de main-d'œuvre.

---

## Article 2 – Durée et volume de prestation

La mission débute le **{{DATE_DEBUT}}** et se termine le **{{DATE_FIN}}** inclus.

Durant cette période, le PRESTATAIRE s'engage à fournir entre **{{JOURS_MIN}}** et **{{JOURS_MAX}}** jours de prestation. Ce volume pourra être ajusté par écrit (avenant ou échange d'e-mails formel) d'un commun accord entre les Parties.

À la fin de chaque mois, le PRESTATAIRE établit un Compte Rendu d'Activité (CRA) récapitulant le nombre de jours réalisés, soumis à la validation du CLIENT. Sans retour motivé du CLIENT sous **{{DELAI_VALIDATION_CRA_JOURS}} jours ouvrés** suivant l'envoi du CRA, celui-ci est réputé validé.

---

## Article 3 – Indépendance, localisation et modalités d'exécution

Le PRESTATAIRE exerce son activité en toute indépendance. Il conserve une entière autonomie dans l'organisation de son travail et de son emploi du temps, sans aucun lien de subordination juridique ou hiérarchique vis-à-vis du CLIENT.

La mission sera exécutée selon les modalités suivantes : **{{MODALITE_LIEU_EXECUTION}}** *(ex : dans les locaux du CLIENT / en télétravail / hybride X jours sur site et Y jours à distance)*.

Lorsque le PRESTATAIRE intervient dans les locaux du CLIENT, il s'engage à respecter les règles d'hygiène, de sécurité et de sûreté applicables sur le site, ainsi que les plages horaires d'ouverture des locaux, sans que cela puisse être interprété comme une soumission au pouvoir de direction du CLIENT.

---

## Article 4 – Attestations réglementaires et assurances

Conformément aux articles L. 8222-1 et D. 8222-5 du Code de travail relatifs à l'obligation de vigilance et à la lutte contre le travail dissimulé (pour tout contrat d'un montant global au moins égal à 5 000 € HT), le PRESTATAIRE s'engage à remettre au CLIENT, à la signature du présent contrat puis tous les six (6) mois jusqu'à son terme, sur demande :
- une attestation de fourniture des déclarations sociales et de paiement des cotisations (attestation de vigilance URSSAF) datant de moins de six (6) mois ;
- un justificatif d'immatriculation à jour (extrait Kbis, avis de situation SIRENE ou extrait du Registre National des Entreprises).

Le PRESTATAIRE déclare être titulaire d'une assurance de Responsabilité Civile Professionnelle (RC Pro) en cours de validité auprès d'une compagnie notoirement solvable, couvrant les dommages matériels et immatériels susceptibles d'être causés dans le cadre de l'exécution de sa mission. Il en produira l'attestation sur simple demande du CLIENT.

---

## Article 5 – Conditions financières

Le prix de la prestation est fixé selon un tarif journalier de **{{TJM_HT}} € hors taxes (HT)**.

Ce montant sera majoré de la TVA au taux légal en vigueur au jour de la facturation *(ou mention « TVA non applicable, art. 293 B du CGI » si le PRESTATAIRE bénéficie de la franchise en base de TVA)*.

Si, à la demande écrite et préalable du CLIENT, le PRESTATAIRE est amené à effectuer des déplacements professionnels spécifiques en dehors du lieu habituel d'exécution de la mission, les frais de transport, d'hébergement et de restauration feront l'objet d'une refacturation séparée au réel, sur présentation des justificatifs.

Toute prestation complémentaire non prévue au présent contrat donnera lieu à une facturation distincte sur la base d'un devis préalable accepté par le CLIENT.

---

## Article 6 – Modalités de facturation et de règlement

La facturation est établie mensuellement, en fin de mois, sur la base du Compte Rendu d'Activité (CRA) validé et joint à la facture.

Le règlement s'effectuera par virement bancaire dans un délai de **{{DELAI_PAIEMENT_JOURS}} jours** *(maximum légal entre professionnels : 60 jours ou 45 jours fin de mois à compter de la date d'émission de la facture, ou 45 jours pour les factures périodiques)* à compter de la date d'émission de la facture.

Conformément aux articles L. 441-10 et D. 441-5 du Code de commerce, tout retard de paiement entraîne de plein droit, le jour suivant la date d'échéance figurant sur la facture et sans qu'un rappel soit nécessaire :
- l'application de pénalités de retard calculées au taux d'intérêt appliqué par la Banque Centrale Européenne (BCE) à son opération de refinancement la plus récente majoré de 10 points de pourcentage *(taux minimum légal : 3 fois le taux d'intérêt légal)* ;
- le paiement d'une indemnité forfaitaire pour frais de recouvrement d'un montant de **40 €** par facture impayée.

En cas de défaut de paiement persistant huit (8) jours après l'envoi d'une mise en demeure restée sans effet, le PRESTATAIRE se réserve le droit de suspendre l'exécution de ses prestations jusqu'au complet règlement des sommes dues, sans que sa responsabilité puisse être engagée à ce titre.

---

## Article 7 – Propriété intellectuelle

### 7.1 Cession des droits sur les développements spécifiques
Sous réserve du **complet paiement** des factures correspondantes, le PRESTATAIRE cède à titre exclusif au CLIENT l'ensemble des droits patrimoniaux de propriété intellectuelle sur les livrables et développements originaux (codes sources spécifiques, documentations, jeux d'essais) réalisés exclusivement pour le CLIENT dans le cadre du présent contrat.

Conformément à l'article L. 131-3 du Code de la propriété intellectuelle, cette cession comprend les droits de reproduction, de représentation, d'adaptation, de modification, de traduction et d'exploitation commerciale ou interne, pour le **monde entier** et pour toute la **durée légale de protection des droits d'auteur**.

### 7.2 Éléments préexistants et savoir-faire
La présente cession ne porte pas sur les méthodes, algorithmes génériques, bibliothèques logicielles, outils ou composants développés par le PRESTATAIRE antérieurement ou indépendamment du présent contrat (*« Éléments Préexistants »*), ni sur les composants tiers ou *open source* soumis à leurs licences propres. Si des Éléments Préexistants du PRESTATAIRE sont intégrés aux livrables, le PRESTATAIRE concède au CLIENT une licence d'utilisation non exclusive, mondiale et perpétuelle sur ceux-ci, strictement limitée aux besoins d'exploitation des livrables.

Le présent contrat n'empêche en aucun cas le PRESTATAIRE de réutiliser librement les connaissances, l'expérience et le savoir-faire acquis lors de la mission pour d'autres clients, y compris dans le même secteur d'activité, sous réserve de ne pas reproduire les éléments originaux et confidentiels développés exclusivement pour le CLIENT.

---

## Article 8 – Confidentialité

Chacune des Parties s'engage à considérer comme strictement confidentielles toutes les informations, données, documents ou méthodes (techniques, commerciales, financières, stratégiques ou nominatives) qui lui seront communiqués par l'autre Partie ou dont elle aura connaissance à l'occasion de l'exécution du présent contrat.

Chaque Partie s'interdit de divulguer à des tiers tout ou partie de ces informations confidentielles sans l'accord écrit préalable de l'autre Partie. Ne sont toutefois pas considérées comme confidentielles les informations tombées dans le domaine public sans faute de la Partie réceptrice, ou dont la divulgation est exigée par la loi ou une autorité judiciaire.

Chaque Partie se porte fort, au sens de l'article 1204 du Code civil, du respect du présent engagement de confidentialité par ses salariés, dirigeants, mandataires ou sous-traitants dûment autorisés.

Cet engagement de confidentialité restera en vigueur pendant toute la durée du contrat et pour une durée de **{{DUREE_CONFIDENTIALITE_ANS}} ans** *(ex : 2 ou 5 ans)* après son expiration ou sa résiliation.

---

## Article 9 – Responsabilité

Le PRESTATAIRE étant soumis à une obligation de moyens, sa responsabilité ne pourra être engagée qu'en cas de faute prouvée dans l'exécution de ses prestations.

En aucun cas, le PRESTATAIRE ne pourra être tenu responsable des dommages indirects subis par le CLIENT (tels que perte de chiffre d'affaires, perte de chance, perte de données, préjudice commercial ou d'image).

En tout état de cause, si la responsabilité du PRESTATAIRE venait à être retenue, le montant total des indemnités et dommages-intérêts qu'il pourrait être amené à verser au CLIENT, toutes causes confondues, est expressément plafonné au montant total des honoraires HT effectivement perçus par le PRESTATAIRE au titre du présent contrat *(ou au cours des {{DUREE_PLAFOND_RESPONSABILITE_MOIS}} derniers mois)*.

---

## Article 10 – Incessibilité et sous-traitance

Sauf accord écrit et préalable de l'autre Partie, le présent contrat est conclu *intuitu personae* et ne peut être cédé, transféré ou sous-traité, en tout ou partie, par aucune des Parties.

---

## Article 11 – Renouvellement et résiliation

### 11.1 Résiliation pour convenance
Le présent contrat pourra être résilié de manière anticipée par le CLIENT moyennant un préavis écrit de **{{PREAVIS_CLIENT_JOURS}} jours**. Si le CLIENT dispense le PRESTATAIRE d'exécuter sa prestation pendant tout ou partie de la durée du préavis, le CLIENT s'engage néanmoins à régler l'intégralité des jours ouvrés couverts par ce préavis au tarif journalier convenu.

Le présent contrat pourra être résilié par le PRESTATAIRE moyennant un préavis écrit de **{{PREAVIS_PRESTATAIRE_JOURS}} jours**, sans indemnité ni compensation financière. Le PRESTATAIRE s'engage à poursuivre sa prestation de bonne foi pendant la durée du préavis.

La durée de ces préavis pourra être réduite d'un commun accord écrit entre les Parties.

### 11.2 Résiliation pour manquement
En cas de manquement grave d'une des Parties à ses obligations contractuelles (notamment en cas de non-paiement des factures par le CLIENT), l'autre Partie pourra résilier le contrat de plein droit quinze (15) jours après l'envoi d'une mise en demeure par lettre recommandée avec accusé de réception (LRAR) restée infructueuse.

### 11.3 Renouvellement
Le présent contrat pourra être renouvelé par accord écrit des deux Parties (avenant ou nouveau bon de commande) au plus tard **{{DELAI_RENOUVELLEMENT_JOURS}} jours** avant son échéance.

---

## Article 12 – Droit applicable et juridiction compétente

Le présent contrat est régi par le droit français.

En cas de différend relatif à l'interprétation, l'exécution ou la résiliation du présent contrat, les Parties s'efforceront de trouver une solution amiable. À défaut d'accord dans un délai de trente (30) jours, le litige sera soumis à la compétence exclusive du **Tribunal de commerce de {{TRIBUNAL_COMPETENT}}**.

---

Fait en deux (2) exemplaires originaux (ou signé électroniquement),  
À **{{VILLE_SIGNATURE}}**, le **{{DATE_SIGNATURE}}**.

| Pour le **PRESTATAIRE** ({{PRESTATAIRE_NOM}}) | Pour le **CLIENT** ({{CLIENT_RAISON_SOCIALE}}) |
| :--- | :--- |
| *Nom et qualité :* {{PRESTATAIRE_REPRESENTANT}} — {{PRESTATAIRE_REPRESENTANT_FONCTION}} | *Nom et qualité :* {{CLIENT_REPRESENTANT}} — {{CLIENT_REPRESENTANT_FONCTION}} |
| *Signature :* | *Signature :* |
