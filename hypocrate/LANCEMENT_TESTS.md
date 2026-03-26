# 🎯 Lancement des Tests Utilisateur - Hypocrate

## ✅ État Actuel

### Documentation Créée
1. ✅ **GUIDE_TEST_UTILISATEUR.md** - Guide complet d'organisation des tests
2. ✅ **DEPLOIEMENT_RAPIDE.md** - Instructions de déploiement
3. ✅ **QUICKSTART_HYPOCRATE.md** - Guide de démarrage rapide
4. ✅ **LANCEMENT_TESTS.md** - Ce fichier (résumé)

### Application
- ✅ Code source complet et fonctionnel
- ✅ Interface Streamlit intuitive
- ✅ Transcription audio (Whisper)
- ✅ Extraction entités médicales (spaCy + scispaCy)
- ✅ Génération SOAP (Ollama + Llama2)
- ✅ Lettre d'adressage automatique
- ✅ Exports multiples (TXT, PDF, DOCX)

---

## 🚀 Démarrage Immédiat

### Option 1 : Local (Recommandé)

```bash
# 1. Aller dans le dossier
cd /Users/xcallens/CascadeProjects/windsurf-project/hypocrate

# 2. Lancer l'application
./start_hypocrate.sh

# 3. Ouvrir le navigateur
# → http://localhost:8501
```

**Pour partager avec testeurs sur le même réseau :**
```bash
# Trouver votre IP
ipconfig getifaddr en0

# Lancer avec accès réseau
streamlit run hypocrate_app.py --server.address 0.0.0.0

# Partager l'URL : http://[VOTRE_IP]:8501
```

---

### Option 2 : Cloud (Tests à Distance)

**Streamlit Cloud (Gratuit) :**

1. **Pousser sur GitHub** (déjà fait ✅)
   ```bash
   git add .
   git commit -m "Préparation tests utilisateur"
   git push origin main
   ```

2. **Déployer sur Streamlit Cloud**
   - Aller sur https://share.streamlit.io
   - Se connecter avec GitHub
   - Cliquer "New app"
   - Repository : `pimvic/Sumy`
   - Branch : `main`
   - Main file : `hypocrate/hypocrate_app.py`
   - Cliquer "Deploy"

3. **URL générée**
   ```
   https://pimvic-sumy-hypocrate.streamlit.app
   ```

**⚠️ Limitations Streamlit Cloud :**
- Ressources limitées (1GB RAM)
- Ollama ne fonctionne pas (nécessite API externe)
- Modèles Whisper légers uniquement (tiny/base)

---

## 📋 Checklist Avant Tests

### Technique
- [ ] Application lance sans erreur
- [ ] Ollama fonctionne : `ollama list`
- [ ] Modèle llama2 téléchargé : `ollama pull llama2`
- [ ] Test upload audio OK
- [ ] Test transcription OK
- [ ] Test génération SOAP OK
- [ ] Test exports OK (TXT, PDF, DOCX)

### Préparation Testeurs
- [ ] Fichiers audio de test créés (3 exemples)
- [ ] Guide utilisateur finalisé
- [ ] Questionnaire de feedback préparé
- [ ] Email d'invitation rédigé
- [ ] Support disponible (email/téléphone)

### Communication
- [ ] Liste testeurs définie (5-10 personnes)
- [ ] Invitations envoyées
- [ ] Planning tests communiqué
- [ ] Canal support actif

---

## 👥 Profil Testeurs Idéal

**5-10 testeurs avec :**
- 2-3 médecins généralistes
- 1-2 spécialistes (cardio, dermato, etc.)
- 1-2 infirmiers/infirmières
- 1 secrétaire médicale

**Critères :**
- Utilise régulièrement un ordinateur
- Fait des consultations quotidiennes
- Intéressé par l'innovation
- Disponible 30-45 minutes

---

## 📧 Template Email Invitation

```
Objet : [Test Utilisateur] Hypocrate - Assistant IA Médical

Bonjour Dr [Nom],

Vous êtes invité(e) à tester Hypocrate, un assistant IA qui transforme 
vos consultations audio en comptes-rendus médicaux structurés (SOAP).

🔗 ACCÈS
[URL de l'application]

📖 GUIDE
Voir pièce jointe : QUICKSTART_HYPOCRATE.pdf

⏱️ DURÉE
30-45 minutes (à votre convenance cette semaine)

🎯 OBJECTIF
- Tester avec 2-3 consultations réelles (anonymisées)
- Remplir le questionnaire de feedback

📋 QUESTIONNAIRE
[Lien Google Forms ou PDF joint]

💬 SUPPORT
En cas de problème :
- Email : support@hypocrate.ai
- Téléphone : 06.XX.XX.XX.XX
- Disponibilité : 9h-18h

Vos retours sont essentiels pour améliorer l'outil !

Merci infiniment,
Xavier Callens
Équipe Hypocrate

---

P.S. : Toutes les données restent 100% locales et confidentielles.
```

---

## 📊 Questionnaire de Feedback

### Questions Clés

**1. Facilité d'utilisation (1-5)**
- Interface intuitive : ⭐⭐⭐⭐⭐
- Clarté des instructions : ⭐⭐⭐⭐⭐
- Fluidité du workflow : ⭐⭐⭐⭐⭐

**2. Qualité Transcription (1-5)**
- Précision globale : ⭐⭐⭐⭐⭐
- Termes médicaux : ⭐⭐⭐⭐⭐
- Gestion accents/bruits : ⭐⭐⭐⭐⭐

**3. Extraction Entités (1-5)**
- Allergies identifiées : ⭐⭐⭐⭐⭐
- Médicaments corrects : ⭐⭐⭐⭐⭐
- Symptômes pertinents : ⭐⭐⭐⭐⭐

**4. Compte-Rendu SOAP (1-5)**
- Structure claire : ⭐⭐⭐⭐⭐
- Contenu pertinent : ⭐⭐⭐⭐⭐
- Utilisable tel quel : ⭐⭐⭐⭐⭐

**5. Questions Ouvertes**
- Ce qui fonctionne bien : _____________
- Ce qui pourrait être amélioré : _____________
- Fonctionnalités manquantes : _____________
- Utiliseriez-vous cet outil ? ☐ Oui ☐ Non
- Prix acceptable : _____ €/mois

---

## 🎯 Critères de Succès

**Le POC est validé si :**
- ✅ 80%+ trouvent l'interface intuitive (≥4/5)
- ✅ 75%+ des transcriptions précises (≥4/5)
- ✅ 70%+ des SOAP utilisables (≥4/5)
- ✅ 60%+ utiliseraient l'outil en pratique
- ✅ <5% de bugs critiques

---

## 📅 Planning Suggéré

### Semaine 1 : Préparation
- **Jour 1-2** : Tests internes (équipe)
- **Jour 3** : Corrections bugs critiques
- **Jour 4-5** : Préparation matériel testeurs

### Semaine 2 : Tests Utilisateurs
- **Jour 1** : Envoi invitations + onboarding
- **Jour 2-4** : Tests actifs + support
- **Jour 5** : Collecte feedbacks

### Semaine 3 : Analyse
- **Jour 1-2** : Analyse résultats
- **Jour 3-4** : Priorisation améliorations
- **Jour 5** : Rapport final + présentation

---

## 🔧 Support Pendant Tests

### Problèmes Courants

**1. Ollama ne démarre pas**
```bash
ollama serve
ollama list
ollama pull llama2
```

**2. Erreur spaCy**
```bash
python -m spacy download fr_core_news_md --force
```

**3. Erreur Whisper**
```bash
pip install --upgrade openai-whisper torch
```

**4. Port 8501 occupé**
```bash
lsof -i :8501
kill -9 [PID]
# ou
streamlit run hypocrate_app.py --server.port 8502
```

### Contact Support
- **Email :** support@hypocrate.ai
- **Téléphone :** [Votre numéro]
- **Disponibilité :** 9h-18h, lundi-vendredi

---

## 📈 Métriques à Suivre

### Quantitatives
- Taux de réussite upload : ____%
- Temps moyen traitement : _____ sec
- Taux d'erreurs : ____%
- Taux de complétion : ____%

### Qualitatives
- Score moyen facilité : ___/5
- Score moyen qualité : ___/5
- Score moyen pertinence : ___/5
- Taux d'adoption potentielle : ____%

---

## 🎁 Fichiers Audio de Test

### Créer 3 Exemples

**1. Consultation Courte (1 min) - Pharyngite**
```
Médecin: Bonjour, qu'est-ce qui vous amène?
Patient: J'ai mal à la gorge depuis 3 jours.
Médecin: Avez-vous de la fièvre?
Patient: Oui, 38°C hier soir.
Médecin: Allergies connues?
Patient: Pénicilline.
Médecin: Je vais examiner. *examine* Gorge rouge. 
         Je prescris du paracétamol. Repos 3 jours.
```

**2. Consultation Moyenne (3 min) - Suivi Diabète**
```
[Dialogue plus long avec antécédents, traitement actuel, 
 résultats analyses, ajustement traitement]
```

**3. Consultation Complexe (5 min) - Multi-pathologies**
```
[Patient avec plusieurs pathologies, interactions 
 médicamenteuses, ajustements multiples]
```

**Outils pour créer les audios :**
- Enregistrement direct (smartphone/micro)
- Synthèse vocale (Google TTS, ElevenLabs)
- Acteurs/collègues qui jouent les rôles

---

## ✅ Actions Immédiates

### Aujourd'hui
1. [ ] Lancer l'application localement
2. [ ] Tester le workflow complet
3. [ ] Créer 3 fichiers audio de test
4. [ ] Finaliser questionnaire feedback

### Demain
1. [ ] Identifier 5-10 testeurs potentiels
2. [ ] Rédiger emails d'invitation
3. [ ] Préparer support (email/téléphone)
4. [ ] Créer formulaire Google Forms

### Cette Semaine
1. [ ] Envoyer invitations
2. [ ] Onboarding testeurs
3. [ ] Support actif pendant tests
4. [ ] Collecte feedbacks quotidienne

---

## 📞 Contact

**Chef de Projet :** Xavier Callens
**Email :** xavier@hypocrate.ai
**GitHub :** https://github.com/pimvic/Sumy
**Documentation :** Voir dossier `hypocrate/`

---

## 🚀 Commande de Lancement

```bash
cd /Users/xcallens/CascadeProjects/windsurf-project/hypocrate
./start_hypocrate.sh
```

**L'application s'ouvrira automatiquement dans votre navigateur !**

---

**Bonne chance pour les tests ! 🏥✨**

*Hypocrate - Transformez vos consultations en documents professionnels*
