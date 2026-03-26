# 🦙 Local LLM Setup & Configuration Guide - Sumy Medical Scribe

## Complete Guide to Running Local Models: Ollama + Whisper

### Table of Contents

1. [Overview & Architecture](#overview--architecture)
2. [Why Local Models Matter](#why-local-models-matter)
3. [Prerequisites & System Requirements](#prerequisites--system-requirements)
4. [Installation Guide](#installation-guide)
5. [Configuration & Setup](#configuration--setup)
6. [Usage Examples](#usage-examples)
7. [Performance Tuning](#performance-tuning)
8. [Troubleshooting](#troubleshooting)
9. [Advanced Customization](#advanced-customization)
10. [Production Deployment](#production-deployment)
11. [Resources & References](#resources--references)

---

## Overview & Architecture

### What is Medical Scribe AI?

**Sumy** (Medical Scribe AI) is a **100% local, privacy-first** medical documentation system that combines:

- **🦙 Large Language Models (Ollama/Llama2/Mistral)** - For generating medical notes from transcripts
- **🎤 Speech Recognition (Whisper)** - For converting audio consultations to text
- **💰 Zero API Costs** - Everything runs on your machine, no cloud subscription fees
- **🔒 Complete Privacy** - Medical data never leaves your computer
- **🚀 Fast Local Processing** - No latency waiting for cloud responses

### System Architecture

```
┌──────────────────────── Medical Scribe AI ────────────────────────┐
│                                                                      │
│  User (Doctor/Medical Professional)                                │
│                    ↓                                                 │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  Hypocrate UI (Streamlit Frontend)                          │  │
│  │  • User-friendly interface                                  │  │
│  │  • Audio recording & playback                               │  │
│  │  • Document editing & export                                │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                    ↓                                                 │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  Medical Scribe API (FastAPI Backend)                       │  │
│  │  • REST endpoints for all operations                         │  │
│  │  • JWT authentication & user management                      │  │
│  │  • Request/response validation                               │  │
│  │  • Database management                                       │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                    ↓                                                 │
│  ┌─────────────── Local AI Processing (100% Private) ──────────┐  │
│  │                                                             │  │
│  │  ┌──────────────────────────────────────────────────────┐  │  │
│  │  │  Whisper (OpenAI)                                    │  │  │
│  │  │  • Local speech recognition engine                   │  │  │
│  │  │  • Converts audio → text transcription               │  │  │
│  │  │  • Runs entirely on your machine                     │  │  │
│  │  │  • No internet required                              │  │  │
│  │  └──────────────────────────────────────────────────────┘  │  │
│  │                                                             │  │
│  │  ┌──────────────────────────────────────────────────────┐  │  │
│  │  │  Ollama + Llama2/Mistral                             │  │  │
│  │  │  • Local LLM inference engine                        │  │  │
│  │  │  • Generates SOAP notes from transcripts             │  │  │
│  │  │  • Performs medical entity extraction                │  │  │
│  │  │  • Customizable medical prompts                      │  │  │
│  │  └──────────────────────────────────────────────────────┘  │  │
│  │                                                             │  │
│  │  ┌──────────────────────────────────────────────────────┐  │  │
│  │  │  NLP Services                                        │  │  │
│  │  │  • scispaCy: Medical NER (Named Entity Recognition)  │  │  │
│  │  │  • spaCy: General NLP processing                     │  │  │
│  │  │  • Automatic medical term extraction                 │  │  │
│  │  └──────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                    ↓                                                 │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  Local SQLite Database                                      │  │
│  │  • Stores all medical notes & transcriptions                │  │
│  │  • User authentication & sessions                           │  │
│  │  • Audio files metadata                                    │  │
│  │  • No external database connections                         │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  🔒 PRIVACY GUARANTEE: No data ever leaves this system             │
│  🚀 PERFORMANCE: All processing happens on your machine            │
│  💰 COST: Zero subscription fees - completely free                 │
│  🔐 SECURITY: HIPAA/GDPR compliant architecture                   │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Why Local Models Matter

### Privacy & Compliance Benefits

**The Privacy Problem with Cloud APIs:**

When using OpenAI or similar cloud services, your medical consultations are:
- ❌ Sent to external servers
- ❌ Stored in cloud databases
- ❌ Processed by third-party systems
- ❌ Potentially retained for training
- ❌ Subject to their privacy policies
- ❌ Exposed to compromise/breaches

**The Local Solution:**

With Sumy's local models:
- ✅ All data stays on your machine
- ✅ Zero external API calls
- ✅ You maintain complete data ownership
- ✅ HIPAA-compliant by architecture
- ✅ Works completely offline
- ✅ No cloud dependencies

**Real-World Example:**

```
Cloud Approach:
User (Local) → Medical Data → Internet → OpenAI Servers → Your Account
                                    ↓
                            Provider's Policies
                            Database Security
                            Staff Access
                            Regulatory Compliance

Local Approach:
User (Local) → Medical Data → Stays Local → Your Control
                                    ↓
                        Your Security Policies
                        Your Backups
                        Your Access Control
```

### Financial Benefits

**Cost Comparison for Medical Practice (100 consultations/month):**

| Cost Category | OpenAI API | Sumy Local |
|---|---|---|
| Transcription (Whisper) | $36 | $0 |
| SOAP Note Generation (GPT-4) | $120 | $0 |
| Monthly Subscription | $20 | $0 |
| **Total Monthly** | **$176** | **$0** |
| **Yearly Savings** | — | **$2,112** |
| 5-Year Savings | — | **$10,560** |

### Performance Benefits

**Response Times Comparison:**

```
OpenAI API:
1. Encode audio in your client
2. Send to OpenAI server in US
3. OpenAI processes
4. Send response back
Total: 5-15 seconds (network dependent)

Local Processing:
1. Process audio locally
2. No network latency
Total: 2-8 seconds (machine dependent)

With GPU: 1-3 seconds
```

---

## Prerequisites & System Requirements

### Minimum System Requirements

**CPU-Only Configuration (Slower but works):**
- **OS:** Windows 10/11, macOS 11+, or Ubuntu 18.04+
- **Processor:** 4-core CPU @ 2.5GHz minimum
- **RAM:** 16GB (8GB minimum for basic operation)
- **Storage:** 50GB free (30GB for models + 20GB for OS)
- **Internet:** Only needed for initial model download

**GPU-Accelerated Configuration (Recommended):**
- **GPU:** NVIDIA GPU with 6GB+ VRAM (CUDA) OR Apple Silicon
- **RAM:** 16GB+ system RAM
- **Storage:** 100GB free (50GB models + OS/data)
- **Drivers:** Latest CUDA/cuDNN (NVIDIA) or metal support (macOS)

### Hardware Recommendations by Use Case

| Scenario | CPU RAM | GPU RAM | Model Size | Notes |
|---|---|---|---|---|
| **Solo Practitioner** | 16GB | CPU only | Llama2 7B | Perfect for 1-5 daily consultations |
| **Small Clinic (5 users)** | 32GB | 8GB | Mistral 7B | Share single Ollama instance |
| **Large Clinic (20+ users)** | 64GB | 12GB | Mixtral 8x7B | Multiple instances with load balancing |
| **Research/Training** | 128GB+ | 24GB+ | Fine-tuned models | Custom medical model training |

### Checking Your System

**macOS:**
```bash
# Check processor
sysctl -n macm.cpu.brand_string

# Check RAM
vm_stat | grep "Pages free"

# Check storage
df -h /

# Check for Apple Silicon (M1/M2)
sysctl -n sysctl.hw.optional.arm64
```

**Linux:**
```bash
# Check CPU
lscpu

# Check RAM
free -h

# Check storage
df -h

# Check GPU
nvidia-smi  # If NVIDIA GPU present
```

**Windows (PowerShell):**
```powershell
# Check processor
Get-WmiObject Win32_Processor | Select Name

# Check RAM
[Math]::Round((Get-WmiObject Win32_OperatingSystem).TotalVisibleMemorySize / 1MB)

# Check storage
Get-Volume | Where {$_.DriveType -eq 'Fixed'}

# Check GPU
Get-WmiObject Win32_VideoController
```

---

## Installation Guide

### Step 1: Install Ollama

**macOS (Easiest):**

```bash
# Option 1: Using Homebrew (recommended)
brew install ollama

# Verify installation
ollama --version
```

**Linux (Debian/Ubuntu):**

```bash
# Download and run installer
curl -fsSL https://ollama.ai/install.sh | sh

# Verify
ollama --version

# Start Ollama service
sudo systemctl start ollama
sudo systemctl enable ollama  # Start on boot
```

**Windows:**

```powershell
# Download from https://ollama.ai/download/windows

# Or using winget
winget install Ollama.Ollama

# Verify
ollama --version

# Ollama runs as Windows service automatically
```

**Docker (For Production/Advanced):**

```bash
# Run Ollama in Docker
docker run -d \
  --name ollama \
  -p 11434:11434 \
  -v ollama-data:/root/.ollama \
  ollama/ollama

# Verify
docker logs ollama

# Pull models
docker exec ollama ollama pull mistral:7b-instruct
```

### Step 2: Download Language Models

**Understanding Model Sizes:**

| Model | Size | Speed | Quality | RAM Needed |
|---|---|---|---|---|
| llama2:latest | 3.8GB | Medium | Good | 8GB |
| mistral:7b-instruct | 4.4GB | Medium | Excellent | 8GB |
| neural-chat:7b | 3.5GB | Medium | Good | 8GB |
| codellama:7b | 3.7GB | Medium | Good | 8GB |
| mixtral:8x7b | 26GB | Slow | Excellent | 32GB+ |

**Download Models:**

```bash
# Primary recommendation for medical use
ollama pull mistral:7b-instruct

# Alternative (faster but lower quality)
ollama pull llama2

# Optional: For coding-related notes
ollama pull codellama:7b

# List what you've downloaded
ollama list
```

**Understanding the Output:**

```
NAME                    ID              SIZE  MODIFIED
mistral:7b-instruct     23bbb93c67ef    4.4GB 2 minutes ago
llama2:latest           78e26419b446    3.8GB 5 minutes ago
```

### Step 3: Download Speech Recognition Model (Whisper)

**Understanding Whisper Models:**

| Model | Size | Speed | Accuracy | RAM |
|---|---|---|---|---|
| tiny | 140MB | 10x faster | ~80% | 1GB |
| base | 140MB | 5x faster | ~85% | 1GB |
| small | 440MB | 2x faster | ~90% | 2GB |
| medium | 1.5GB | Same speed | ~95% | 5GB |
| large | 2.9GB | Slower | ~96% | 10GB |

**Install Whisper:**

```bash
# Install from OpenAI
pip install openai-whisper

# Or from source
pip install git+https://github.com/openai/whisper.git

# Verify installation
whisper --version

# Pre-download language model
whisper --model base --language en /dev/null
# This downloads the model for faster later use
```

### Step 4: Install Python Dependencies

**Create Virtual Environment:**

```bash
# Navigate to project
cd /path/to/Sumy

# Create Python environment
python3.10 -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Upgrade pip
pip install --upgrade pip setuptools wheel
```

**Install Medical Scribe Dependencies:**

```bash
# Install all requirements
pip install -r requirements.txt

# Key packages installed:
# - fastapi: Web API framework
# - sqlalchemy: Database ORM
# - ollama: Ollama Python client
# - openai-whisper: Speech recognition
# - scispacy: Medical NLP
# - pydantic: Data validation

# Verify key installations
python -c "import ollama; print('Ollama OK')"
python -c "import whisper; print('Whisper OK')"
python -c "import scispacy; print('scispaCy OK')"
```

**Install scispaCy Medical Models:**

```bash
# Medical NER model (for entity extraction)
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_core_sci_md-0.5.1.tar.gz

# Verify
python -c "import spacy; nlp = spacy.load('en_core_sci_md'); print('Medical NLP ready')"
```

### Step 5: Configure Environment

**Create .env file:**

```bash
# Navigate to project directory
cd /path/to/Sumy/medical-scribe

# Create .env file
cat > .env << EOF
# Core Configuration
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=INFO

# Ollama Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=mistral:7b-instruct
OLLAMA_EMBEDDING_MODEL=nomic-embed-text

# Whisper Configuration
USE_LOCAL_WHISPER=true
WHISPER_MODEL=base
WHISPER_DEVICE=cpu  # or 'cuda' if NVIDIA GPU available
WHISPER_LANGUAGE=en

# Database
DATABASE_URL=sqlite:///./medical_scribe.db

# API
API_PORT=8001
API_HOST=127.0.0.1

# Security
SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_urlsafe(32))')
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8501

# Frontend (Streamlit)
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=localhost

EOF

# Protect .env file
chmod 600 .env
```

**Verify Configuration:**

```bash
# Load .env and verify
python3 << 'EOF'
import os
from dotenv import load_dotenv

load_dotenv()

print("Configuration Check:")
print(f"Ollama URL: {os.getenv('OLLAMA_BASE_URL')}")
print(f"Model: {os.getenv('OLLAMA_MODEL')}")
print(f"Whisper Model: {os.getenv('WHISPER_MODEL')}")
print(f"Database: {os.getenv('DATABASE_URL')}")
print("✅ Configuration loaded successfully!")
EOF
```

---

## Configuration & Setup

### Starting All Services

**Option 1: Manual Start (Development)**

```bash
# Terminal 1: Start Ollama service
ollama serve

# Wait for output like: "Listening on 127.0.0.1:11434"

# Terminal 2: Start Medical Scribe API
cd /path/to/Sumy/medical-scribe
source venv/bin/activate
python -m uvicorn backend.app.main:app --reload --port 8001

# Terminal 3: Start Streamlit UI
cd /path/to/Sumy/hypocrate
streamlit run hypocrate_app.py --server.port=8501
```

**Option 2: Docker Compose (Production)**

```bash
# Navigate to project root
cd /path/to/Sumy

# Create docker-compose.yml
cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  ollama:
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    environment:
      - OLLAMA_HOST=0.0.0.0:11434
    command: serve

  medical-scribe-api:
    build:
      context: ./medical-scribe
      dockerfile: Dockerfile
    ports:
      - "8001:8001"
    environment:
      - OLLAMA_BASE_URL=http://ollama:11434
      - OLLAMA_MODEL=mistral:7b-instruct
      - WHISPER_MODEL=base
      - DATABASE_URL=sqlite:///./medical_scribe.db
    depends_on:
      - ollama
    volumes:
      - ./medical-scribe:/app

  hypocrate-ui:
    build:
      context: ./hypocrate
      dockerfile: Dockerfile
    ports:
      - "8501:8501"
    environment:
      - API_URL=http://medical-scribe-api:8001
    depends_on:
      - medical-scribe-api

volumes:
  ollama_data:

EOF

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Verify Everything is Working

**Test Ollama Connection:**

```bash
# Check if Ollama is responding
curl http://localhost:11434/api/tags

# Should return:
# {"models":["mistral:7b-instruct","llama2:latest"]}

# If error, Ollama is not running
```

**Test Whisper Installation:**

```bash
# Test transcription
whisper --model base --language en --output_format txt << 'EOF'
# This is a test audio file
EOF

# Or test with actual audio
whisper test_audio.wav --model base
```

**Test API Startup:**

```bash
# Check if API is responding
curl http://localhost:8001/docs

# Should open Swagger documentation
# If error, API is not running
```

**Run Comprehensive Test:**

```bash
# Navigate to project
cd /path/to/Sumy/medical-scribe

# Run test script
python3 << 'EOF'
import os
import json

print("=" * 50)
print("Medical Scribe AI - Local Setup Test")
print("=" * 50)

# Test 1: Ollama connection
print("\n1. Testing Ollama...")
try:
    import requests
    response = requests.get("http://localhost:11434/api/tags")
    if response.status_code == 200:
        models = response.json().get('models', [])
        print(f"   ✅ Ollama is running")
        print(f"   📦 Available models: {len(models)}")
        for model in models:
            print(f"      - {model['name']}")
    else:
        print(f"   ❌ Ollama error: {response.status_code}")
except Exception as e:
    print(f"   ❌ Ollama not running: {e}")

# Test 2: Whisper installation
print("\n2. Testing Whisper...")
try:
    import whisper
    print(f"   ✅ Whisper installed: {whisper.__version__}")
except ImportError:
    print(f"   ❌ Whisper not installed")

# Test 3: scispaCy
print("\n3. Testing Medical NLP...")
try:
    import spacy
    nlp = spacy.load("en_core_sci_md")
    print(f"   ✅ Medical NLP model loaded")
except Exception as e:
    print(f"   ❌ Medical NLP error: {e}")

# Test 4: Environment variables
print("\n4. Checking configuration...")
from dotenv import load_dotenv
load_dotenv()

config_keys = [
    "OLLAMA_BASE_URL",
    "OLLAMA_MODEL",
    "WHISPER_MODEL",
    "DATABASE_URL"
]

for key in config_keys:
    value = os.getenv(key)
    if value:
        print(f"   ✅ {key}: {value}")
    else:
        print(f"   ⚠️  {key}: NOT SET")

print("\n" + "=" * 50)
print("Setup check complete!")
print("=" * 50)
EOF
```

---

## Usage Examples

### Example 1: Basic Medical Note Generation

```python
from backend.app.services.medical_notes import MedicalNoteService
from backend.app.config import get_settings

settings = get_settings()

# Initialize service
note_service = MedicalNoteService(settings)

# Sample doctor-patient conversation
transcript = """
Doctor: Good morning. What brings you in today?
Patient: I've had a persistent cough for about two weeks now.
Doctor: Any fever or chills?
Patient: Yes, I had a low-grade fever yesterday, maybe 99.5 degrees.
Doctor: Any shortness of breath?
Patient: Only when I exercise, not at rest.
Doctor: Have you been exposed to sick contacts?
Patient: My colleague has been sick for a month.
Doctor: Any allergies?
Patient: Just penicillin - causes rash.
Doctor: I'm going to examine you. Listen to your lungs... clear bilaterally. Your heart sounds normal.
I'm prescribing an inhaled steroid and decongestant. Follow up in one week.
"""

# Generate SOAP note
soap_note = note_service.generate_soap_note(transcript)

print("Generated SOAP Note:")
print(f"Subjective: {soap_note['subjective']}")
print(f"Objective: {soap_note['objective']}")
print(f"Assessment: {soap_note['assessment']}")
print(f"Plan: {soap_note['plan']}")
```

### Example 2: Audio Transcription Workflow

```python
import os
from backend.app.services.transcription import TranscriptionService
from backend.app.config import get_settings

settings = get_settings()

# Initialize service
transcription_service = TranscriptionService(settings)

# Transcribe audio file
audio_file = "consultation_recording.wav"

if os.path.exists(audio_file):
    result = transcription_service.transcribe_audio(audio_file)
    
    print(f"Transcription completed in {result['duration_seconds']:.1f} seconds")
    print(f"Text length: {len(result['text'])} characters")
    print(f"\nTranscribed text:")
    print(result['text'])
    
    # Save transcription
    with open("transcript.txt", "w") as f:
        f.write(result['text'])
else:
    print(f"Error: {audio_file} not found")
```

### Example 3: End-to-End Medical Documentation

```python
from fastapi import FastAPI, UploadFile
from backend.app.services.transcription import TranscriptionService
from backend.app.services.medical_notes import MedicalNoteService
from backend.app.services.ner import MedicalNERService
from backend.app.config import get_settings

settings = get_settings()

# Initialize all services
transcription_svc = TranscriptionService(settings)
note_svc = MedicalNoteService(settings)
ner_svc = MedicalNERService(settings)

async def process_consultation(audio_file: UploadFile):
    \"\"\"Complete workflow: Audio → Transcript → SOAP Note → Entities\"\"\"
    
    # Step 1: Transcribe audio
    print("Step 1: Transcribing audio...")
    with open("temp_audio.wav", "wb") as tmp:
        tmp.write(await audio_file.read())
    
    transcript_result = transcription_svc.transcribe_audio("temp_audio.wav")
    transcript_text = transcript_result['text']
    print(f"✅ Transcription complete: {transcript_result['duration_seconds']}s")
    
    # Step 2: Generate SOAP note
    print("Step 2: Generating SOAP note...")
    soap_result = note_svc.generate_soap_note(transcript_text)
    print(f"✅ SOAP note generated")
    
    # Step 3: Extract medical entities
    print("Step 3: Extracting medical entities...")
    entities = ner_svc.extract_entities(soap_result['soap_note'])
    print(f"✅ Found {len(entities)} entities")
    
    # Step 4: Compile results
    medical_document = {
        "transcription\": transcript_text,
        "soap_note\": soap_result['soap_note'],
        "entities\": {
            \"conditions\": entities.get('conditions', []),
            \"medications\": entities.get('medications', []),
            \"procedures\": entities.get('procedures', [])
        }
    }
    
    return medical_document
```

---

## Performance Tuning

### Optimizing for Your Hardware

**For CPU-Only Systems (8-16GB RAM):**

```bash
# Use lightweight model
OLLAMA_MODEL=mistral:7b

# Limit context window
# In backend/app/services/ollama_service.py
num_ctx = 2048  # Smaller context = faster inference

# Use tiny Whisper model
WHISPER_MODEL=tiny
```

**For Systems with NVIDIA GPU:**

```bash
# Install CUDA support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Larger context window is possible
num_ctx = 4096

# Use larger Whisper model for better accuracy
WHISPER_MODEL=medium

# Configuration in .env
WHISPER_DEVICE=cuda
```

**For Apple Silicon (M1/M2) Macs:**

```bash
# Metal support is built-in with Ollama
# Performance is excellent - uses GPU automatically

# You can use larger models
OLLAMA_MODEL=mistral:7b-instruct

# Whisper also uses Metal
WHISPER_DEVICE=mps  # Metal Performance Shaders
```

### Benchmarking Your Setup

```python
#!/usr/bin/env python3
import time
from backend.app.services.transcription import TranscriptionService
from backend.app.services.medical_notes import MedicalNoteService
from backend.app.config import get_settings

settings = get_settings()

print("Performance Benchmark")
print("=" * 50)

# Benchmark 1: Whisper Transcription
print("\n1. Speech Recognition (Whisper)")
print("-" * 30)

transcript_svc = TranscriptionService(settings)
audio_file = "test_audio.wav"  # ~1 minute

start = time.time()
result = transcript_svc.transcribe_audio(audio_file)
duration = time.time() - start

print(f"Duration: {duration:.2f} seconds")
print(f"Real-time factor: {result['duration_seconds'] / duration:.2f}x")
print(f"Character count: {len(result['text'])}")

# Benchmark 2: Note Generation
print("\n2. Medical Note Generation (LLM)")
print("-" * 30)

note_svc = MedicalNoteService(settings)
transcript = result['text']

start = time.time()
soap_result = note_svc.generate_soap_note(transcript)
duration = time.time() - start

print(f"Duration: {duration:.2f} seconds")
print(f"Output length: {len(soap_result['soap_note'])} characters")
print(f"Speed: {len(soap_result['soap_note']) / duration:.0f} chars/sec")

# Benchmark 3: End-to-End
print("\n3. Complete Workflow")
print("-" * 30)

start = time.time()
# Transcribe
trans = transcription_svc.transcribe_audio(audio_file)
# Generate note
note = note_svc.generate_soap_note(trans['text'])
duration = time.time() - start

print(f"Total time: {duration:.2f} seconds")
print(f"For 30-minute consultation: {duration * 2:.0f} seconds (~{duration * 2 / 60:.0f} minutes)")
```

---

## Troubleshooting

### Common Issues & Solutions

**Issue 1: "Connection refused" when accessing Ollama**

```bash
# Problem: Ollama service not running

# Solution 1: Start Ollama
ollama serve

# Solution 2: Check if already running
ps aux | grep ollama

# Solution 3 (Linux): Check service status
sudo systemctl status ollama

# Solution 4 (Docker): Check container
docker ps | grep ollama

# Solution 5: Verify port is open
curl -v http://localhost:11434/api/tags
```

**Issue 2: Model not found / "model not found"**

```bash
# Problem: Model not downloaded yet

# Solution: Pull the model
ollama pull mistral:7b-instruct
ollama pull llama2

# Verify models are present
ollama list

# Expected output:
# NAME                    ID          SIZE  MODIFIED
# mistral:7b-instruct     23bb...     4.4GB 2 min ago
```

**Issue 3: "Out of memory" errors during note generation**

```bash
# Solution 1: Use smaller model
OLLAMA_MODEL=llama2  # Smaller than Mistral

# Solution 2: Reduce context window
# In ollama_service.py
num_ctx = 1024  # Instead of 4096

# Solution 3: Monitor memory usage
# macOS
vm_stat 1 | grep "Pages free"

# Linux
watch -n 1 'free -h'

# Windows PowerShell
while(1) { Get-WmiObject Win32_OperatingSystem | Select @{N='FreeMemoryGB';E={[math]::Round($_.FreePhysicalMemory/1MB)}} | ft -AutoSize; sleep 1 }
```

**Issue 4: Slow transcription / note generation**

```bash
# Problem: Processing is taking too long

# Solution 1: Use GPU acceleration
# Edit .env
WHISPER_DEVICE=cuda  # For NVIDIA GPUs
WHISPER_DEVICE=mps   # For Apple Silicon

# Solution 2: Use smaller models
WHISPER_MODEL=tiny
OLLAMA_MODEL=llama2

# Solution 3: Batch processing
# Process multiple files in sequence instead of parallel

# Solution 4: Check system resources
# Monitor CPU/GPU/Memory usage while processing
```

**Issue 5: Whisper not working / "pip install openai-whisper" fails**

```bash
# Problem: Whisper installation failed

# Solution 1: Complete fresh install
pip uninstall openai-whisper
pip cache purge
pip install openai-whisper --upgrade

# Solution 2: With specific Python version
python3.10 -m pip install openai-whisper

# Solution 3: From source
pip install git+https://github.com/openai/whisper.git@main

# Solution 4: Verify installation
python -c "import whisper; print(whisper.__version__)"

# Solution 5: Check for ffmpeg (required dependency)
ffmpeg -version
# If not installed:
# macOS: brew install ffmpeg
# Linux: sudo apt install ffmpeg
# Windows: choco install ffmpeg
```

**Issue 6: Database errors / "database is locked"**

```bash
# Problem: SQLite database locked by another process

# Solution 1: Stop multiple servers
# Check for duplicate API instances
ps aux | grep uvicorn

# Kill duplicate
kill -9 <PID>

# Solution 2: Remove lock file
rm -f /path/to/medical_scribe.db-wal
rm -f /path/to/medical_scribe.db-shm

# Solution 3: Check database integrity
sqlite3 ./medical_scribe.db "PRAGMA integrity_check;"

# Solution 4: Restart API
# In terminal running API, press Ctrl+C
# Then restart
python -m uvicorn backend.app.main:app --reload
```

### Performance Troubleshooting

**Diagnose Slow Performance:**

```bash
#!/bin/bash
# performance_check.sh

echo "=== System Performance Check ==="

echo "\n1. CPU Usage"
top -n 1 -b | head -15

echo "\n2. Memory Usage"
free -h

echo "\n3. Process Information"
ps aux | grep -E "(ollama|uvicorn|streamlit)"

echo "\n4. Network I/O"
netstat -an | grep LISTEN

echo "\n5. Disk I/O"
iostat -x 1 2

echo "\n6. Model Status"
curl -s http://localhost:11434/api/tags | python3 -m json.tool

echo "\n=== Analysis ==="
echo "If you see high CPU without GPU usage: Try using GPU"
echo "If memory is high: Use smaller models"
echo "If disk I/O is high: May be swapping (not enough RAM)"
```

---

## Advanced Customization

### Creating Custom Medical Models

**Fine-tune Ollama for Your Specialty:**

```bash
# 1. Create Modelfile for specialty
cat > Modelfile-Cardiology << 'EOF'
FROM mistral:7b-instruct

# Custom system prompt for cardiology
SYSTEM You are an expert medical scribe specializing in cardiology. \
When analyzing patient consultations:
- Focus on cardiovascular symptoms and findings
- Use proper cardiac terminology
- Structure SOAP notes for cardiac conditions
- Include relevant cardiac measurements and tests
- Recommend appropriate cardiac interventions

# Tuning parameters
PARAMETER temperature 0.3
PARAMETER top_p 0.9
PARAMETER num_ctx 2048

# System prompt for medical accuracy
EOF

# 2. Create the custom model
ollama create cardiology-scribe -f Modelfile-Cardiology

# 3. Use in .env
echo "OLLAMA_MODEL=cardiology-scribe" >> .env

# 4. Verify
ollama list | grep cardiology
```

### Custom Prompts for Different Specialties

```python
# backend/app/services/medical_notes.py

SYSTEM_PROMPTS = {
    "general": """You are a professional medical scribe. Generate SOAP notes...""",
    
    "cardiology": """You are an expert cardiac scribe. Focus on:
    - ECG findings
    - Cardiac biomarkers
    - Echocardiography results
    - Coronary artery disease assessment
    - Heart failure staging
    - Arrhythmia management
    """,
    
    "neurology": """You are an expert neurology scribe. Focus on:
    - Neurological examination findings
    - Seizure characterization
    - Headache classification
    - Neuroimaging interpretation
    - Medication management for neurological conditions
    """,
    
    "orthopedics": """You are an expert orthopedic scribe. Focus on:
    - Joint examination findings
    - Imaging interpretation (X-ray, MRI)
    - Surgical options
    - Physical therapy recommendations
    - Functional limitations assessment
    """,
}

def generate_soap_note_specialty(transcript: str, specialty: str):
    system_prompt = SYSTEM_PROMPTS.get(specialty, SYSTEM_PROMPTS["general"])
    # Use custom prompt for specialty
    return generate_soap_note(transcript, system_prompt=system_prompt)
```

---

## Production Deployment

### Docker Deployment

**Dockerfile for Production:**

```dockerfile
# backend/Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY backend/ .

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8001/health || exit 1

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
```

**Production Docker Compose:**

```yaml
version: '3.8'

services:
  ollama:
    image: ollama/ollama:latest
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
    volumes:
      - ollama_data:/root/.ollama
    networks:
      - medical-scribe
    restart: unless-stopped

  api:
    build:
      context: ./medical-scribe
      dockerfile: Dockerfile
    ports:
      - "8001:8001"
    depends_on:
      - ollama
    networks:
      - medical-scribe
    restart: unless-stopped
    environment:
      - OLLAMA_BASE_URL=http://ollama:11434
      - ENVIRONMENT=production

  nginx:
    image: nginx:alpine
    ports:
      - "443:443"
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - /etc/letsencrypt:/etc/letsencrypt
    depends_on:
      - api
    networks:
      - medical-scribe
    restart: unless-stopped

volumes:
  ollama_data:

networks:
  medical-scribe:
```

### Scaling Considerations

**For Multiple Concurrent Users:**

```python
# Load balancing multiple Ollama instances
from ollama import Client

class LoadBalancedOllamaService:
    def __init__(self, instances: list = None):
        self.instances = instances or [
            "http://ollama-1:11434",
            "http://ollama-2:11434",
            "http://ollama-3:11434",
        ]
        self.current = 0
    
    def _get_next_instance(self):
        instance = self.instances[self.current % len(self.instances)]
        self.current += 1
        return instance
    
    def generate(self, prompt: str) -> str:
        instance = self._get_next_instance()
        client = Client(host=instance)
        return client.generate(prompt)
```

---

## Resources & References

### Official Documentation

- **Ollama:** https://ollama.ai/docs
- **Whisper:** https://github.com/openai/whisper
- **Llama2:** https://www.llama.com/
- **Mistral:** https://docs.mistral.ai/
- **FastAPI:** https://fastapi.tiangolo.com/
- **Streamlit:** https://docs.streamlit.io/
- **SQLAlchemy:** https://docs.sqlalchemy.org/

### Papers & Research

- **Whisper:** [Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/abs/2212.04356)
- **Llama2:** [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/abs/2307.09288)
- **Mistral:** [Mistral 7B](https://arxiv.org/abs/2310.06825)

### Community & Support

- **GitHub Issues:** https://github.com/pimvic/Sumy/issues
- **Discussions:** https://github.com/pimvic/Sumy/discussions
- **Ollama Community:** https://github.com/ollama/ollama/discussions
- **Hugging Face Models:** https://huggingface.co/

### Learning Resources

- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/20/orm/)
- [Streamlit Documentation](https://docs.streamlit.io/en/stable/)
- [Privacy in Medical AI](https://www.ibm.com/topics/healthcare-data-security)
- [HIPAA Compliance Guide](https://www.hhs.gov/hipaa/for-professionals/index.html)

---

<div align=\"center\">

## 🚀 Ready to Get Started?

### Complete Setup in 5 Steps:

1. **Install Ollama** - `brew install ollama` (or download)
2. **Download Models** - `ollama pull mistral:7b-instruct`
3. **Install Python Deps** - `pip install -r requirements.txt`
4. **Configure .env** - `cp .env.example .env`
5. **Start Services** - `ollama serve` + `uvicorn` + `streamlit`

### Get Help:

- **Questions?** [GitHub Discussions](https://github.com/pimvic/Sumy/discussions)
- **Issues?** [GitHub Issues](https://github.com/pimvic/Sumy/issues)
- **Docs?** [Full Documentation](https://github.com/pimvic/Sumy/wiki)

---

**Your complete local medical scribe is ready! 🎉**

*Privacy. Performance. Complete Control.*

</div>
"