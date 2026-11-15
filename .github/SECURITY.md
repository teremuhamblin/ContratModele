# ContratModele

---

### Fichier `/SECURITY.md`
### 🔒 Politique de sécurité
– v1.0

La sécurité et la fiabilité de **ContratModele** recouvrent à la fois la protection des données personnelles, l'intégrité des fichiers du dépôt et le respect des droits des tiers.

---

## 📦 Versions supportées

| Version | Statut |
| :--- | :--- |
| **v1.0.x** | ✅ Supportée (mises à jour de sécurité et correctifs) |
| **< v1.0** | ❌ Non supportée |

---

## 🚨 Que faut-il signaler via ce canal privé ?

Merci d'utiliser la procédure de signalement privé (et **non** une *Issue* publique) uniquement pour les sujets sensibles suivants :

1. **Fuite de données personnelles ou confidentielles (PII) :** présence accidentelle d'un vrai nom, d'un numéro SIRET, d'une adresse, d'un e-mail, de coordonnées bancaires ou d'un document client réel dans les fichiers ou dans l'historique Git.

2. **Vulnérabilité technique :** faille de sécurité dans d'éventuels scripts d'outillage (génération PDF, CI/CD GitHub Actions), lien malveillant ou injection dans un fichier Markdown.

3. **Atteinte aux droits d'auteur / demande de retrait :** présence non autorisée d'un texte protégé appartenant à un tiers nécessitant une suppression ou une réécriture rapide.

> 💡 **Note :** Pour une simple erreur juridique, une clause obsolète ou une coquille, ouvrez plutôt une **Issue publique** ou une **Pull Request** classique (voir [CONTRIBUTING.md](CONTRIBUTING.md)).

---

## 📩 Comment signaler un problème sensible ?

**N'ouvrez pas d'Issue publique** afin d'éviter de propager des données sensibles ou une faille exploitable.

Veuillez utiliser l'un des deux canaux suivants :
1. **Signalement privé GitHub (recommandé) :** Rendez-vous dans l'onglet **Security** du dépôt → **Advisories** → **Report a vulnerability**.

2. **Par e-mail :** Contactez le mainteneur à l'adresse **[votre-email-securite@exemple.com]** avec pour objet `[SECURITY] ContratModele - <résumé court>`.

Merci d'inclure dans votre message :
- le chemin du fichier ou le *commit* concerné ;
- une description claire du problème ou des données exposées ;
- toute preuve ou recommandation utile pour la correction.

---

## ⏱️ Traitement et délais de réponse

- **Accusé de réception :** sous **72 heures** ouvrées maximum.
- **Analyse et remédiation :** en cas de fuite de données personnelles ou de contenu protégé, le fichier incriminé sera corrigé et, si nécessaire, **l'historique Git sera nettoyé** dans les plus brefs délais.
- Un avis de correction pourra être publié après résolution si la situation l'exige.

---

## 🛡️ Bonnes pratiques pour les utilisateurs des modèles

- **Ne remplissez jamais un contrat dans un fork public GitHub :** si vous forkez ce dépôt pour personnaliser vos contrats avec vos informations réelles (identité, SIRET, TJM, nom de vos clients), passez votre dépôt en **privé** ou travaillez **en local** avant d'exporter en PDF.

- **Vérifiez l'intégrité avant signature :** relisez systématiquement l'ensemble du document généré (notamment les champs `[...]` ou `XXXX`, les tarifs et les renvois d'articles) avant de l'envoyer pour signature à un client.
