# 🚀 Déploiement Rapide - Hypocrate pour Tests Utilisateur

## ✅ Ce qui a été préparé

### 1. Documentation Complète
- ✅ `GUIDE_TEST_UTILISATEUR.md` - Guide complet pour organiser les tests
- ✅ `QUICKSTART_HYPOCRATE.md` - Guide de démarrage rapide
- ✅ `README.md` - Documentation technique
- ✅ `start_hypocrate.sh` - Script de lancement automatique

### 2. Application Prête
- ✅ Interface Streamlit complète
- ✅ Transcription audio (Whisper)
- ✅ Extraction d'entités médicales (spaCy + scispaCy)
- ✅ Génération SOAP (Ollama + Llama2)
- ✅ Lettre d'adressage automatique

---

## 🎯 Options de Déploiement

### Option 1 : Local (Recommandé pour POC)

**Avantages :**
- ✅ Contrôle total
- ✅ Performances optimales
- ✅ Données 100% locales (confidentialité)
- ✅ Pas de coûts

**Commandes :**
```bash
cd /Users/xcallens/CascadeProjects/windsurf-project/hypocrate
./start_hypocrate.sh
```

**Accès :**
- Local : http://localhost:8501
- Réseau : http://[VOTRE_IP]:8501

**Partage avec testeurs :**
```bash
# Trouver votre IP
ipconfig getifaddr en0

# Lancer avec accès réseau
streamlit run hypocrate_app.py --server.address 0.0.0.0
```

---

### Option 2 : Streamlit Cloud (Tests à Distance)

**Avantages :**
- ✅ Gratuit
- ✅ URL publique partageable
- ✅ Déploiement en 5 minutes

**Limitations :**
- ⚠️ Ressources limitées (1GB RAM)
- ⚠️ Ollama ne fonctionne pas (nécessite API cloud)
- ⚠️ Modèles Whisper légers uniquement

**Étapes :**

1. **Créer configuration Streamlit Cloud**
```bash
mkdir -p .streamlit
cat > .streamlit/config.toml << 'EOF'
[server]
headless = true
port = 8501
maxUploadSize = 200

[theme]
primaryColor = "#4CAF50"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
EOF
```

2. **Créer fichier packages.txt** (dépendances système)
```bash
cat > packages.txt << 'EOF'
ffmpeg
libsndfile1
EOF
```

3. **Modifier requirements pour cloud**
```bash
cat > requirements_cloud.txt << 'EOF'
streamlit>=1.28.0
openai-whisper
torch
torchaudio
spacy>=3.7.0
scispacy
pydub
python-docx
reportlab
requests
EOF
```

4. **Se connecter à Streamlit Cloud**
- Aller sur https://share.streamlit.io
- Se connecter avec GitHub
- New app → `pimvic/Sumy`
- Main file : `hypocrate/hypocrate_app.py`
- Deploy !

**URL générée :**
```
https://pimvic-sumy-hypocrate.streamlit.app
```

---

### Option 3 : Docker (Portable)

**Avantages :**
- ✅ Environnement isolé
- ✅ Déploiement reproductible
- ✅ Peut héberger Ollama

**Créer Dockerfile :**
```dockerfile
FROM python:3.10-slim

# Installer dépendances système
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Installer Ollama
RUN curl -fsSL https://ollama.ai/install.sh | sh

# Copier application
WORKDIR /app
COPY requirements_hypocrate.txt .
RUN pip install --no-cache-dir -r requirements_hypocrate.txt

# Télécharger modèles spaCy
RUN python -m spacy download fr_core_news_md
RUN python -m spacy download en_core_web_sm

COPY . .

# Exposer port
EXPOSE 8501

# Lancer Ollama et Streamlit
CMD ollama serve & \
    sleep 5 && \
    ollama pull llama2 && \
    streamlit run hypocrate_app.py --server.address 0.0.0.0
```

**Commandes Docker :**
```bash
# Build
docker build -t hypocrate .

# Run
docker run -p 8501:8501 hypocrate

# Accès : http://localhost:8501
```

---

## 📊 Recommandations par Cas d'Usage

### Cas 1 : Tests avec 1-3 médecins en présentiel
**Solution :** Local sur votre machine
```bash
./start_hypocrate.sh
```
- Montrez l'écran aux testeurs
- Ou partagez via réseau local

### Cas 2 : Tests avec 5-10 médecins à distance
**Solution :** Streamlit Cloud
- URL publique partageable
- Pas de configuration pour testeurs
- ⚠️ Prévenir des limitations (modèles légers)

### Cas 3 : Tests intensifs / Production
**Solution :** Serveur dédié (AWS/GCP) + Docker
- Performances optimales
- Contrôle total
- Coût : ~50-100€/mois

---

## 🔧 Résolution Problèmes Courants

### Problème : Ollama ne démarre pas
```bash
# Vérifier si Ollama est installé
ollama --version

# Installer si nécessaire
brew install ollama  # macOS
# ou https://ollama.ai

# Démarrer manuellement
ollama serve
```

### Problème : Modèle Llama2 manquant
```bash
ollama pull llama2
ollama list  # Vérifier
```

### Problème : Erreur spaCy
```bash
python -m spacy download fr_core_news_md --force
python -m spacy download en_core_web_sm --force
```

### Problème : Erreur Whisper/PyTorch
```bash
pip install --upgrade torch torchaudio
pip install --upgrade openai-whisper
```

### Problème : Port 8501 déjà utilisé
```bash
# Trouver processus
lsof -i :8501

# Tuer processus
kill -9 [PID]

# Ou utiliser autre port
streamlit run hypocrate_app.py --server.port 8502
```

---

## 📝 Checklist Avant Tests

### Technique
- [ ] Application lance sans erreur
- [ ] Ollama fonctionne (`ollama list`)
- [ ] Modèle llama2 téléchargé
- [ ] Upload fichier audio OK
- [ ] Transcription fonctionne
- [ ] SOAP généré correctement
- [ ] Exports fonctionnent (TXT, PDF, DOCX)

### Organisationnel
- [ ] URL de test partagée
- [ ] Guide utilisateur envoyé
- [ ] Fichiers audio de test préparés
- [ ] Questionnaire de feedback créé
- [ ] Support disponible (email/téléphone)
- [ ] Planning tests défini

### Communication
- [ ] Email d'invitation rédigé
- [ ] Instructions claires envoyées
- [ ] Rappel 24h avant tests
- [ ] Canal support actif

---

## 📧 Template Email Invitation

```
Objet : [Test Utilisateur] Hypocrate - Assistant IA Médical

Bonjour Dr [Nom],

Vous êtes invité(e) à tester Hypocrate, un assistant IA qui transforme 
vos consultations audio en comptes-rendus médicaux structurés.

🔗 ACCÈS À L'APPLICATION
[Insérer URL]

📖 GUIDE D'UTILISATION
[Lien vers QUICKSTART_HYPOCRATE.md]

⏱️ DURÉE DU TEST
30-45 minutes (à votre convenance cette semaine)

🎯 OBJECTIF
Tester avec 2-3 consultations réelles (anonymisées) et nous faire 
vos retours via le questionnaire.

📋 QUESTIONNAIRE
[Lien vers formulaire Google Forms ou PDF]

💬 SUPPORT
En cas de problème : support@hypocrate.ai ou 06.XX.XX.XX.XX

Merci infiniment pour votre participation ! Vos retours sont 
essentiels pour améliorer l'outil.

Cordialement,
Xavier Callens
Équipe Hypocrate
```

---

## 🎯 Métriques de Succès

**Le POC est validé si :**
- ✅ 80%+ trouvent l'interface intuitive (≥4/5)
- ✅ 75%+ des transcriptions précises (≥4/5)
- ✅ 70%+ des SOAP utilisables (≥4/5)
- ✅ 60%+ utiliseraient l'outil en pratique
- ✅ <5% de bugs critiques

---

## 📞 Support

**Pendant les tests :**
- Email : support@hypocrate.ai
- Téléphone : [Votre numéro]
- Disponibilité : 9h-18h, lundi-vendredi

**Après les tests :**
- Rapport complet sous 48h
- Présentation résultats sous 1 semaine
- Roadmap améliorations sous 2 semaines

---

## 🚀 Prochaines Étapes

1. **Aujourd'hui :** Lancer l'application localement
2. **J+1 :** Tests internes (équipe projet)
3. **J+2-3 :** Corrections bugs critiques
4. **J+4 :** Envoi invitations testeurs
5. **J+5-10 :** Tests utilisateurs actifs
6. **J+11-12 :** Analyse résultats
7. **J+13 :** Présentation rapport final

---

**Bonne chance ! 🏥🚀**

Pour toute question : xavier@hypocrate.ai
GitHub : https://github.com/pimvic/Sumy
