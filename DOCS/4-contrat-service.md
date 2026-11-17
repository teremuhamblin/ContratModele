> ⚠️ **Avertissement :** Modèle fourni à titre purement informatif (droit français). Il ne constitue pas un conseil juridique ; faites-le relire par un professionnel du droit avant signature.

> **Note d'utilisation (à supprimer avant envoi) :**
> - Contrat de prestation de conseil / service **au forfait et par phases** entre deux sociétés B2B, avec cahier des charges en annexe.
> - Utilisez `python3 scripts/generate.py` ou remplacez chaque variable `{{...}}` par les valeurs convenues, et ne conservez que l'option choisie là où plusieurs choix sont proposés (ex : Sous-traitance).

---

# Contrat de prestation de services

**Entre les soussignés :**

La société **{{CLIENT_RAISON_SOCIALE}}**, {{CLIENT_FORME_JURIDIQUE}} au capital de **{{CLIENT_CAPITAL_EUR}} €**, dont le siège social est situé **{{CLIENT_ADRESSE}}**, immatriculée au Registre du Commerce et des Sociétés de **{{CLIENT_RCS_VILLE}}** sous le numéro **{{CLIENT_SIREN}}**, représentée par **{{CLIENT_REPRESENTANT}}**, en qualité de **{{CLIENT_REPRESENTANT_FONCTION}}**, dûment habilité(e) aux fins des présentes,  
*(ci-après dénommée « **le Client** »)*,

**d'une part,**

**et**

La société **{{PRESTATAIRE_NOM}}**, {{PRESTATAIRE_FORME_JURIDIQUE}} au capital de **{{PRESTATAIRE_CAPITAL_EUR}} €**, dont le siège social est situé **{{PRESTATAIRE_ADRESSE}}**, immatriculée au Registre du Commerce et des Sociétés de **{{PRESTATAIRE_RCS_VILLE}}** sous le numéro **{{PRESTATAIRE_SIREN}}**, représentée par **{{PRESTATAIRE_REPRESENTANT}}**, en qualité de **{{PRESTATAIRE_REPRESENTANT_FONCTION}}**, dûment habilité(e) aux fins des présentes,  
*(ci-après dénommée « **le Prestataire** »)*,

**d'autre part,**

*(ci-après désignées ensemble « **les Parties** » et individuellement « **une Partie** »)*.

---

## Préambule

{{CONTEXTE_PREAMBULE}} *(rappeler ici, en quelques lignes, le contexte du projet et les raisons qui motivent l'accord intervenu entre les Parties ; ce préambule fait partie intégrante du contrat et pourra servir à son interprétation en cas de besoin).*

**Ceci exposé, il a été convenu ce qui suit :**

---

## Article 1 – Objet

Le présent contrat est un contrat de prestation de conseil et de services informatiques ayant pour objet la réalisation, par le Prestataire pour le compte du Client, de la mission définie au cahier des charges figurant en **Annexe** du présent contrat et en faisant partie intégrante.

---

## Article 2 – Durée

Le présent contrat est conclu pour une durée de **{{DUREE_MISSION}}** *(ex : 6 mois / 1 an / pour la durée nécessaire à l'exécution de la mission)*. Il prend effet le **{{DATE_DEBUT}}** et arrivera à son terme prévisionnel le **{{DATE_FIN}}**, sauf prolongation ou résiliation anticipée dans les conditions prévues aux présentes.

---

## Article 3 – Conditions financières

### 3.1 Prix forfaitaire et échéancier
En contrepartie de la réalisation des prestations définies à l'Article 1, le Client versera au Prestataire la somme forfaitaire de **{{MONTANT_FORFAIT_HT}} euros hors taxes (€ HT)**, majorée de la TVA au taux légal en vigueur au jour de la facturation *(ou mention « TVA non applicable, art. 293 B du CGI » le cas échéant)*.

Sauf stipulation différente au cahier des charges, ce montant est ventilé selon l'échéancier suivant :
- **20 %** à la signature des présentes *(acompte de démarrage)* ;
- **30 %** à l'issue de **{{JALON_ECHEANCE_2}}** *(ex : la phase intermédiaire / validation du pré-rapport / à J+X suivant la signature)* ;
- **50 %** constituant le solde, à la réception définitive des livrables finaux.

### 3.2 Frais annexes
Les frais de déplacement, d'hébergement, de restauration et frais spécifiques engagés par le Prestataire et strictement nécessaires à l'exécution de la prestation en dehors de ses locaux seront facturés en sus au Client, au réel et sur présentation de justificatifs, sous réserve de l'accord préalable et écrit du Client.

### 3.3 Modalités de règlement et pénalités de retard
Les factures sont payables par virement bancaire dans un délai de **{{DELAI_PAIEMENT_JOURS}} jours** à compter de leur date d'émission *(dans les limites légales prévues à l'article L. 441-10 du Code de commerce : 60 jours ou 45 jours fin de mois maximum)*.

Conformément aux articles L. 441-10 et D. 441-5 du Code de commerce, tout retard de paiement entraîne de plein droit, dès le jour suivant la date d'échéance et sans qu'un rappel soit nécessaire :
- l'exigibilité de pénalités de retard calculées au taux d'intérêt appliqué par la Banque Centrale Européenne (BCE) à son opération de refinancement la plus récente majoré de 10 points de pourcentage *(sans pouvoir être inférieur à 3 fois le taux d'intérêt légal)* ;
- le versement d'une indemnité forfaitaire pour frais de recouvrement de **40 euros** par facture impayée.

En outre, en cas de non-paiement persistant huit (8) jours après mise en demeure écrite restée sans effet, le Prestataire se réserve le droit de suspendre l'exécution de la mission jusqu'au règlement intégral des sommes dues, les délais contractuels étant décalés d'autant.

---

## Article 4 – Exécution de la prestation

### 4.1 Moyens mis en œuvre
Le Prestataire s'engage à mener à bien la mission précisée à l'Article 1, conformément aux règles de l'art et en toute indépendance dans l'organisation de ses moyens. À cet effet, il affecte l'équipe ou les compétences nécessaires à la réalisation de la mission et remet, avant le rapport ou livrable final, une pré-étude au plus tard le **{{DATE_PRE_ETUDE}}**.

### 4.2 Obligation de collaboration du Client
Le Client tiendra à la disposition du Prestataire toutes les informations, données et accès pouvant contribuer à la bonne réalisation de l'objet du présent contrat. À cette fin, le Client désigne un ou plusieurs interlocuteurs privilégiés : **{{CLIENT_INTERLOCUTEUR_PROJET}}**, investis du pouvoir de décision pour assurer le suivi et la validation des diverses étapes de la mission.

*(Facultatif :)* Pour les besoins stricts de la mission, le Client accorde au Prestataire un accès contrôlé et sécurisé aux systèmes et catégories d'informations définis au cahier des charges, dans le respect des règles de sécurité et de confidentialité convenues.

### 4.3 Validation des étapes et réception
À la date prévue pour chaque jalon *(et notamment à la remise du pré-rapport prévue le **{{DATE_LIVRABLE_INTERMEDIAIRE}}**)*, le Client procède à la vérification des travaux remis. Le Client dispose d'un délai de **{{DELAI_RECETTE_JOURS}} jours ouvrés** à compter de la remise du livrable pour formuler par écrit ses réserves motivées ou prononcer sa validation expresse afin que la phase suivante puisse recevoir exécution. À défaut de réponse motivée dans ce délai, le livrable est réputé validé.

---

## Article 5 – Calendrier et délais

Sous réserve du respect par le Client de ses obligations de collaboration et de validation dans les délais convenus à l'Article 4, le calendrier prévisionnel de la mission est le suivant :
- **Phase 1** (définie au cahier des charges) : achèvement au plus tard le **{{DATE_PHASE_1}}** ;
- **Phase 2** (assortie de la remise du pré-rapport) : achèvement au plus tard le **{{DATE_PHASE_2}}** ;
- **Phase 3** (livrables finaux / rapport terminal) : délivrance au plus tard le **{{DATE_PHASE_3}}**.

Tout retard imputable au Client dans la fourniture des informations, accès ou validations entraînera de plein droit un report équivalent des échéances du calendrier ci-dessus.

---

## Article 6 – Nature des obligations et responsabilité

Pour l'accomplissement des diligences et prestations prévues à l'Article 1, le Prestataire s'engage à donner ses meilleurs soins, conformément aux règles de l'art. La présente obligation n'est, de convention expresse, qu'une **obligation de moyens** *(ou : obligation de résultat quant à la conformité des livrables aux spécifications du cahier des charges, selon la nature de la mission)*.

La responsabilité du Prestataire ne peut être engagée qu'en cas de faute prouvée lui étant directement imputable. En aucun cas, le Prestataire ne pourra être tenu responsable des dommages indirects subis par le Client (perte de chiffre d'affaires, de clientèle, de données ou atteinte à l'image).

En toute hypothèse (sauf faute lourde ou dolosive), la responsabilité cumulée du Prestataire au titre du présent contrat, toutes causes confondues, est **plafonnée au montant total hors taxes perçu par le Prestataire au titre du présent contrat**.

---

## Article 7 – Assurance qualité, RC Pro et vigilance sociale

Le Prestataire s'engage à maintenir des processus et standards de qualité conformes aux usages professionnels pour l'exécution des prestations désignées aux présentes.

Il déclare être titulaire d'une assurance Responsabilité Civile Professionnelle (RC Pro) en cours de validité couvrant les dommages susceptibles d'être causés dans le cadre de la mission et en justifiera sur simple demande du Client.

Conformément aux articles L. 8222-1 et D. 8222-5 du Code du travail (pour tout contrat d'un montant global d'au moins 5 000 € HT), le Prestataire remettra au Client, à la signature puis tous les six (6) mois jusqu'au terme du contrat, son attestation de vigilance URSSAF à jour et un justificatif d'immatriculation (extrait Kbis ou RNE).

---

## Article 8 – Obligation de confidentialité

Chacune des Parties considérera comme strictement confidentiels et s'interdit de divulguer à des tiers, sans l'accord écrit préalable de l'autre Partie, toute information, document, donnée ou concept de nature technique, commerciale ou financière dont elle pourra avoir connaissance à l'occasion du présent contrat. Pour l'application de la présente clause, chaque Partie répond de ses salariés, dirigeants et sous-traitants autorisés (article 1204 du Code civil).

Toutefois, aucune des Parties ne saurait être tenue responsable de la divulgation d'éléments qui :
- étaient déjà dans le domaine public à la date de leur communication ou le sont devenus sans faute de sa part ;
- étaient déjà licitement connus de la Partie réceptrice antérieurement à la signature du présent contrat ;
- ont été obtenus de tiers de manière légitime et sans obligation de confidentialité ;
- doivent être communiqués en vertu d'une obligation légale ou d'une décision judiciaire.

La présente obligation perdurera pendant toute la durée du contrat et pendant **{{DUREE_CONFIDENTIALITE_ANS}} ans** *(ex : 5 ans)* après son terme ou sa résiliation.

---

## Article 9 – Propriété des résultats et propriété intellectuelle

De convention expresse, **sous réserve du paiement intégral du prix de la prestation**, le Prestataire cède à titre exclusif au Client les droits patrimoniaux de propriété intellectuelle sur les résultats, rapports et livrables originaux conçus et développés spécifiquement pour le Client dans le cadre du présent contrat.

Conformément à l'article L. 131-3 du Code de la propriété intellectuelle, cette cession couvre les droits de reproduction, de représentation, d'adaptation et d'exploitation pour les besoins de l'activité du Client, pour le **monde entier** et pour toute la **durée légale de protection des droits d'auteur**. Le prix forfaitaire prévu à l'Article 3 inclut le prix de cette cession.

La présente cession ne porte pas sur les méthodes, outils, savoir-faire généraux et briques logicielles développés antérieurement ou indépendamment par le Prestataire, qui demeurent sa propriété exclusive (une licence d'utilisation non exclusive étant concédée au Client pour les seuls besoins d'exploitation des résultats livrés). Le Prestataire s'interdit d'utiliser ou de reproduire pour des tiers les livrables spécifiques réalisés exclusivement pour le Client, sauf autorisation écrite préalable de ce dernier.

---

## Article 10 – Pénalités de retard *(Clause facultative)*

En cas de dépassement des délais impératifs stipulés à l'Article 5 exclusivement imputable au Prestataire *(à l'exclusion de tout retard du Client ou cas de force majeure)*, le Client pourra appliquer, après mise en demeure restée infructueuse pendant huit (8) jours, une pénalité forfaitaire de **{{PENALITE_RETARD_JOURNALIERE}}** *(ex : 0,5 % du montant HT de la phase en retard)* par jour calendaire de retard.

De convention expresse entre les Parties, le montant cumulé des pénalités de retard ne pourra en aucun cas excéder **{{PLAFOND_PENALITES_RETARD_PCT}} %** *(ex : 5 ou 10)* du montant total HT du contrat.

---

## Article 11 – Sous-traitance

*(Ne conserver qu'une seule des deux options ci-dessous et supprimer l'autre :)*

- **Option A (Sous-traitance autorisée pour un tiers identifié) :** Les tâches précisées à l'Article 1 concernant **{{PHASES_SOUS_TRAITEES}}** pourront être exécutées par la société **{{SOUS_TRAITANT_NOM}}**, en qualité de sous-traitant, ce que reconnaît et accepte expressément le Client. Le Prestataire demeure seul responsable envers le Client de la bonne exécution des prestations sous-traitées. Toute autre sous-traitance est soumise à l'accord écrit préalable du Client.
- **Option B (Sous-traitance interdite sauf accord) :** Le présent contrat étant conclu *intuitu personae*, le Prestataire s'interdit de sous-traiter à quiconque tout ou partie de la réalisation des travaux définis à l'Article 1 sans l'accord préalable et écrit du Client.

---

## Article 12 – Résiliation pour manquement

Tout manquement grave de l'une ou l'autre des Parties aux obligations essentielles qu'elle a en charge aux termes du présent contrat (et notamment aux Articles 1, 3, 4, 5, 8 et 9) entraînera, si bon semble au créancier de l'obligation inexécutée, la résiliation de plein droit du présent contrat, **quinze (15) jours** après l'envoi d'une mise en demeure d'exécuter par lettre recommandée avec accusé de réception (LRAR) demeurée sans effet, sans préjudice de tous dommages et intérêts éventuels.

---

## Article 13 – Clause d'imprévision (*Hardship*)

Les Parties reconnaissent que le présent accord constitue une **base équitable et raisonnable** de leur coopération à la date de sa signature.

Conformément à l'article 1195 du Code civil, dans le cas où un changement de circonstances imprévisible lors de la conclusion du contrat rendrait son exécution excessivement onéreuse pour une Partie qui n'avait pas accepté d'en assumer le risque, celle-ci peut demander une renégociation du contrat à son cocontractant, tout en continuant à exécuter ses obligations durant la renégociation.

La Partie qui souhaite se prévaloir de la présente clause en avisera l'autre Partie par lettre recommandée avec accusé de réception dans un délai raisonnable *(ex : trente (30) jours)* suivant la survenance de l'événement, en précisant la nature du changement de circonstances, son impact économique chiffré et une proposition d'ajustement. À défaut d'accord dans un délai de trente (30) jours, les Parties pourront convenir de la résolution du contrat ou demander d'un commun accord au juge de procéder à son adaptation.

---

## Article 14 – Force majeure

Conformément à l'article 1218 du Code civil, aucune des Parties ne sera tenue responsable d'un retard ou d'une inexécution résultant d'un événement de force majeure (événements imprévisibles, irrésistibles et extérieurs tels que guerre, catastrophe naturelle, épidémie ou mesure gouvernementale impérative, incendie, panne généralisée des réseaux).

La Partie qui constate un cas de force majeure doit en informer l'autre Partie par écrit (e-mail confirmé par LRAR) dans les meilleurs délais. Les délais prévus pour la livraison sont automatiquement suspendus et décalés en fonction de la durée de la force majeure. Si l'empêchement perdure au-delà de trente (30) jours, chaque Partie pourra résilier le contrat de plein droit par notification écrite, sans indemnité, les prestations déjà réalisées restant dues.

---

## Article 15 – Loi applicable, langue et juridiction compétente

Le présent contrat est régi par le **droit français**. Le texte rédigé en langue **française** fait foi comme texte original.

En cas de contestation ou de différend découlant du présent contrat ou s'y rapportant, les Parties s'efforceront de trouver une solution amiable dans un délai de trente (30) jours. À défaut d'accord amiable, tout litige relatif à sa validité, son interprétation, son exécution ou sa résiliation sera soumis à la compétence exclusive du **Tribunal de commerce de {{TRIBUNAL_COMPETENT}}**.

*(Note : Pour des contrats internationaux de montant très élevé, cette clause peut être remplacée par une clause d'arbitrage CCI.)*

---

Fait à **{{VILLE_SIGNATURE}}**, le **{{DATE_SIGNATURE}}**, en **deux (2)** exemplaires originaux *(ou signé électroniquement)*.

| Pour le **Prestataire** ({{PRESTATAIRE_NOM}}) | Pour le **Client** ({{CLIENT_RAISON_SOCIALE}}) |
| :--- | :--- |
| *Nom et qualité :* {{PRESTATAIRE_REPRESENTANT}} — {{PRESTATAIRE_REPRESENTANT_FONCTION}} | *Nom et qualité :* {{CLIENT_REPRESENTANT}} — {{CLIENT_REPRESENTANT_FONCTION}} |
| *Signature :* | *Signature :* |
