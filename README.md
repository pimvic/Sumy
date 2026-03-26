# 🏥 Medical Scribe AI - Sumy

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29+-red.svg)](https://streamlit.io/)

> **100% Local AI Medical Assistant** - Transform medical consultations into professional clinical documents with zero API costs

---

## 🎯 Overview

**Medical Scribe AI** is a comprehensive AI-powered medical assistant solution that runs **entirely locally** on your machine. No data leaves your computer, guaranteeing **complete privacy** and **GDPR compliance** while maintaining medical data confidentiality.

### What You'll Learn

This project demonstrates:
- **Modern backend architecture** using FastAPI with REST API principles
- **Local AI integration** with open-source models (Whisper, Llama2)
- **Full-stack Python development** with authentication, database design, and deployment strategies
- **NLP techniques** for medical document generation and named entity recognition
- **Security best practices** for handling sensitive medical data
- **Frontend development** with Streamlit for rapid prototyping
- **DevOps and deployment** strategies for AI applications

### ✨ Two Complementary Applications

| 🔧 **Medical Scribe API** | 🎨 **Hypocrate UI** |
|---------------------------|------------------|
| **Purpose**: Developer-focused backend service | **Purpose**: End-user medical interface |
| **Architecture**: FastAPI REST API with 11 endpoints | **Framework**: Streamlit web application |
| **Authentication**: Multi-user JWT-based system | **Simplicity**: Direct usage without authentication |
| **Persistence**: SQLite database with full history | **Stateless**: No data persistence required |
| **Use Case**: Integration with existing EHR/EMR systems | **Use Case**: Standalone clinical tool |
| **Scalability**: Suitable for enterprise deployment | **Accessibility**: Quick prototyping and demos |

---

## 🚀 Quick Start Guide

### Prerequisites

Before running this project, ensure you have:

```bash
# Verify Python version (3.10 or higher required)
python3 --version
# Output should be: Python 3.10.x or higher

# Install Ollama (local LLM runtime)
# macOS: brew install ollama
# Linux: curl https://ollama.ai/install.sh | sh
# Windows: Download from https://ollama.ai

# Pull Llama2 model (7B parameter version, ~4GB)
ollama pull llama2
# This provides local text generation without API calls
```

### Installation & Setup

#### Option 1: Medical Scribe API (Backend)

This option sets up a production-ready API server suitable for integration with existing medical systems.

```bash
# Clone and navigate to project
git clone https://github.com/pimvic/Sumy.git
cd Sumy/medical-scribe

# Create virtual environment (Python virtual environments isolate dependencies)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies specified in requirements.txt
pip install --upgrade pip
pip install -r requirements.txt

# Initialize environment configuration
./setup_env.sh

# Start the API server (runs on localhost:8001)
./start_server.sh

# Access interactive API documentation
# Browser: http://localhost:8001/docs (Swagger UI)
# Alternative: http://localhost:8001/redoc (ReDoc)
```

#### Option 2: Hypocrate UI (Frontend)

This option provides a simple web interface for medical professionals without technical background.

```bash
# Navigate to Hypocrate directory
cd Sumy/hypocrate

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements_hypocrate.txt

# Download NLP model for French medical text processing
python -m spacy download fr_core_news_md

# Start Streamlit application (runs on localhost:8501)
./start_hypocrate.sh

# Open in browser: http://localhost:8501
```

---

## 📋 Features Explained

### Medical Scribe API (Backend) - Learning Focus

**11 RESTful API Endpoints** following best practices:
- ✅ **Authentication Endpoints**: JWT-based user authentication, secure token generation
  - *Learning: How to implement secure authentication in Python with bcrypt and JWT*
- ✅ **Recording Management**: Upload, retrieve, and manage audio recordings
  - *Learning: File upload handling, validation, and secure storage*
- ✅ **Transcription Service**: Convert audio to text using Whisper AI
  - *Learning: Audio processing pipeline, ML model integration, error handling*
- ✅ **Medical Notes Generation**: Create structured clinical documents using LLMs
  - *Learning: Prompt engineering, LLM integration, output validation and parsing*
- ✅ **Database Layer**: Persistent storage with SQLAlchemy ORM
  - *Learning: Database design, migrations, ACID properties, query optimization*

**Security Features**:
- ✅ JWT-based authentication for multi-user systems
- ✅ Password hashing using bcrypt (cryptographic best practices)
- ✅ User isolation - each user accesses only their own data
- ✅ Local SQLite database - no external dependencies
- ✅ API rate limiting and validation with Pydantic

**Developer Tools**:
- ✅ Interactive Swagger documentation auto-generated from code
- ✅ ReDoc alternative documentation view
- ✅ Standardized JSON API responses
- ✅ Comprehensive error handling and logging

### Hypocrate (User Interface) - Clinical Application

**Streamlit-based Web Application** for medical professionals:
- ✅ **Intuitive Interface**: Upload and analyze consultations in minutes
  - *Learning: Building web UIs with Python using Streamlit's reactive framework*
- ✅ **Automatic Transcription**: Converts speech to text locally
  - *Learning: Audio processing, real-time transcription, performance optimization*
- ✅ **Medical Named Entity Recognition (NER)**: Identifies medications, conditions, dosages
  - *Learning: NLP techniques for domain-specific text analysis*
- ✅ **SOAP Note Generation**: Structured clinical documentation following medical standards
  - *Learning: Medical informatics, clinical documentation standards, structured data generation*
- ✅ **Referral Letter Generation**: Professional formatted letters for patient referrals
  - *Learning: Document templating, business logic for content generation*
- ✅ **Security Alerts**: Highlights drug interactions and allergy warnings
  - *Learning: Business logic, data validation, clinical decision support*
- ✅ **Visualization**: Rich text, tables, and structured data display
  - *Learning: Frontend data visualization and user experience design*

---

## 🏗️ Architecture Explained

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│           MEDICAL SCRIBE AI - SUMY                  │
│              (Fully Local System)                   │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌──────────────────────┐  ┌──────────────────┐   │
│  │   Medical Scribe     │  │   Hypocrate UI   │   │
│  │   API (FastAPI)      │  │   (Streamlit)    │   │
│  │                      │  │                  │   │
│  │  - REST Endpoints    │  │  - Web Interface │   │
│  │  - Multi-user        │  │  - Single User   │   │
│  │  - JWT Auth          │  │  - No Auth       │   │
│  │  - SQLite DB         │  │  - No Persistence│   │
│  └──────────┬───────────┘  └────────┬─────────┘   │
│             │                       │              │
│  ┌──────────▼───────────────────────▼──────┐      │
│  │   AI/ML Services (100% Local)           │      │
│  ├────────────────────────────────────────┤      │
│  │                                         │      │
│  │  🎙️  Speech to Text                    │      │
│  │      • Whisper (OpenAI - Local)        │      │
│  │      • Converts audio to text          │      │
│  │      • Supports 99 languages          │      │
│  │                                         │      │
│  │  📝 Text Generation & Analysis         │      │
│  │      • Llama2 (Meta - Local via Ollama)│      │
│  │      • Generates clinical documents    │      │
│  │      • Supports prompt engineering     │      │
│  │                                         │      │
│  │  🔍 Medical NLP (Named Entity Recog.)  │      │
│  │      • scispaCy (biomedical NLP)      │      │
│  │      • Identifies medical terms        │      │
│  │      • Extracts medications/dosages    │      │
│  │                                         │      │
│  └─────────────────────────────────────────┘      │
│                                                     │
│  ✅ Key Advantage: No internet, no API fees,      │
│     complete data privacy on your machine         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Technology Stack Breakdown

**Backend Framework**:
- **FastAPI** - Modern Python web framework (released 2018)
  - *Learning: Async/await for concurrent request handling, dependency injection pattern*
  - Auto-generates interactive API documentation
  - Type hints for runtime validation via Pydantic

**Database Layer**:
- **SQLAlchemy** - Python ORM (Object-Relational Mapping)
  - *Learning: Database abstraction, migrations, relationships between tables*
- **SQLite** - Embedded SQL database
  - *Learning: ACID properties, transaction management, schema design*

**Authentication & Security**:
- **JWT (JSON Web Tokens)** - Stateless authentication
  - *Learning: Token-based auth vs. session-based, security considerations*
- **bcrypt** - Password hashing algorithm
  - *Learning: Cryptographic basics, salts, computational cost factors*
- **Pydantic** - Data validation library
  - *Learning: Schema validation, type checking at runtime*

**AI/ML (100% Local)**:
- **Whisper** - Speech recognition
  - *Learning: Audio encoding, spectrogram processing, transformer models*
- **Llama2** via **Ollama** - Large Language Model
  - *Learning: LLM architecture, quantization for local execution, prompt design*
- **scispaCy** - Biomedical NLP
  - *Learning: Named Entity Recognition, domain-specific language processing*

**Frontend**:
- **Streamlit** - Rapid web app framework for data science
  - *Learning: Reactive programming model, component lifecycle, state management*

---

## 💡 Use Cases & Implementation

### Use Case 1: Medical Scribe API - Enterprise Integration

**Scenario**: A clinic wants to integrate AI transcription into their existing hospital information system (HIS).

**Implementation**:
```bash
# Step 1: Deploy Medical Scribe API on clinic server
cd medical-scribe && ./start_server.sh

# Step 2: Integrate with HIS using REST API
# The clinic's system makes HTTP requests to our API:

# Authenticate doctor
POST /api/auth/login
Content-Type: application/json
{
  "email": "dr.smith@clinic.com",
  "password": "secure_password"
}
# Returns: {"access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...", "token_type": "bearer"}

# Step 3: Upload consultation recording
POST /api/recordings/upload
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
Content-Type: multipart/form-data
file: @/path/to/consultation.wav
# Returns: {"id": "rec_123", "status": "uploaded", "filename": "consultation.wav"}

# Step 4: Start transcription
POST /api/recordings/rec_123/transcribe
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
# Returns: {"id": "rec_123", "status": "transcribing"}

# Step 5: Generate medical notes
POST /api/recordings/rec_123/generate_medical_notes
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
Content-Type: application/json
{ "note_type": "soap" }
# Returns: {"soap_note": "S: Patient reports...", "timestamp": "2024-03-26T..."}
```

**Learning Outcomes**:
- Understanding REST API design principles
- Implementing secure file uploads with validation
- Async task processing and job queuing
- Error handling and response standardization

### Use Case 2: Hypocrate - Clinical Practice

**Scenario**: A solo practitioner wants a simple tool to document consultations quickly.

**Workflow**:
1. Open Hypocrate web interface (http://localhost:8501)
2. Click "Upload Audio File" button
3. Select recorded consultation (supports: WAV, MP3, M4A)
4. Click "Analyze" button
5. View automatically generated:
   - Transcription of consultation
   - Extracted medical entities (medications, conditions)
   - SOAP-formatted clinical note
   - Referral letter template
6. Copy/modify and save to patient file

**Learning Outcomes**:
- Building user-friendly interfaces with Streamlit
- Integrating multiple AI models in a pipeline
- Handling medical data securely
- Designing clinical workflows for various specialties

---

## 🔒 Security & Privacy Architecture

### ✅ Security Guarantees

The system provides multiple layers of security:

**Data Isolation**:
| Aspect | Guarantee | Implementation |
|--------|-----------|-----------------|
| **100% Local Processing** | No data sent to external servers | All models run locally via Ollama, Whisper, scispaCy |
| **GDPR Compliance** | Full control over patient data | Users manage their own databases |
| **Medical Confidentiality** | No third-party access | No API keys needed, no cloud services |
| **Zero API Costs** | No recurring fees | Open-source models with local execution |

**Authentication & Authorization**:

```python
# Example: Secure user authentication flow
from fastapi_jwt_auth import AuthJWT

@app.post("/login")
async def login(credentials: LoginRequest):
    # Step 1: Verify user exists and credentials match
    user = db.query(User).filter(User.email == credentials.email).first()
    
    # Step 2: Use bcrypt to verify password (never store plaintext!)
    if not bcrypt.verify(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Step 3: Generate JWT token valid for 24 hours
    token = create_access_token(user.id)
    
    # Step 4: Return token (never the password)
    return {"access_token": token, "token_type": "bearer"}

# All subsequent requests require this token:
@app.get("/api/recordings")
async def list_recordings(Depends(verify_jwt_token)):
    # Token is verified here; user_id is extracted
    recordings = db.query(Recording).filter(
        Recording.user_id == current_user_id
    ).all()
    # User only sees THEIR recordings due to user_id filter
```

**Medical Scribe API Specific**:
- ✅ JWT-based multi-user authentication
- ✅ Bcrypt password hashing (one-way encryption)
- ✅ User data isolation via database queries
- ✅ Local SQLite database (never transmitted)

**Encryption Considerations**:
- Passwords: Hashed with bcrypt (not encrypted - hashing is one-way)
- Database: Consider full-disk encryption on server
- API: Use HTTPS in production (not HTTP)
- Backup: Encrypt backups of SQLite database

---

## 💰 Economic Analysis

### Cost Comparison: Traditional API vs. Local Solution

For a clinic processing 1,000 medical consultations per month:

| Component | OpenAI API | Sumy (Local) | Monthly Savings | Annual Savings |
|-----------|-----------|--------------|-----------------|----------------|
| **Transcription** (Whisper) | $360 | $0 | $360 | $4,320 |
| **Text Generation** (GPT-3.5) | $1,200 |$0 | $1,200 | $14,400 |
| **Infrastructure** | $100 | $0 | $100 | $1,200 |
| **Total/Month** | **$1,660** | **$0** | **$1,660** | **$19,920** |

**Additional Benefits**:
- ✅ No per-request API fees
- ✅ No data transmission costs
- ✅ No subscription requirements
- ✅ No vendor lock-in

**Hardware Investment** (One-time):
- An M1 Mac Mini: ~$600 (can process ~3,000 consultations/month)
- Break-even in just **2 weeks** vs. cloud APIs
- Available, unlimited consultations after break-even point

---

## 📊 Performance Characteristics

### Processing Speed Analysis

Tested on MacBook Pro M1 (16GB RAM), single-core execution:

| Consultation Duration | Transcription Time | Document Generation | Total Time | Throughput |
|----------------------|-------------------|-------------------|-----------|-----------|
| **1 minute** | ~10 seconds | ~15 seconds | ~25 seconds | 2.4 docs/min |
| **3 minutes** | ~30 seconds | ~15 seconds | ~45 seconds | 1.3 docs/min |
| **5 minutes** | ~50 seconds | ~20 seconds | ~70 seconds | 0.86 docs/min |
| **10 minutes** | ~100 seconds | ~25 seconds | ~125 seconds | 0.48 docs/min |

**Key Insights**:
- Transcription scales linearly with audio duration
- Document generation is relatively constant (~15-25s)
- Bottleneck: Whisper transcription for longer recordings
- GPU acceleration would provide 3-5x speedup

### Performance Optimization Strategies

**Implemented Optimizations**:
```python
# Strategy 1: Model caching - load once on startup, reuse
class TranscriptionService:
    _model = None  # Loaded only once
    
    @classmethod
    def get_model(cls):
        if cls._model is None:
            cls._model = whisper.load_model("base.en")
        return cls._model

# Strategy 2: Batch processing for multiple files
# Process 10 files simultaneously instead of sequentially
# Result: 10x throughput improvement (limited by API tokens/second)

# Strategy 3: Model quantization - smaller model size
# Use 'tiny' model instead of 'large'
# Trade-off: faster (10x) but less accurate
```

### Scaling Recommendations

| Scenario | Recommended Setup | Expected Throughput |
|----------|------------------|-------------------|
| **Solo Practice** (5-10 docs/day) | Single M1 Mac | Adequate |
| **Group Practice** (50-100 docs/day) | M2 Pro Mac + GPU | Good |
| **Clinic (100-500 docs/day)** | Custom Linux server + RTX GPU | Excellent |
| **Hospital (500+ docs/day)** | Cluster with load balancing | Production-ready |

---

## 📚 Learning Resources & Documentation

### Quick Start Guides
- 📖 **[API Quick Start](./medical-scribe/QUICKSTART.md)** - How to use the REST API
- 🎨 **[Hypocrate Quick Start](./hypocrate/README.md)** - Using the web interface
- 🏥 **[Complete Architecture](./PROJET_COMPLET.md)** - Deep dive into system design

### Technical Deep Dives
- 🔧 **[Local LLM Configuration](./LOCAL_LLM_GUIDE.md)** - Setting up Ollama and Llama2
- 🔌 **[Port Configuration](./PORT_CONFIGURATION.md)** - Network setup and troubleshooting
- 🧪 **[API Testing Guide](./USER_TEST_GUIDE.md)** - Comprehensive test examples
- 📊 **[Test Results & Benchmarks](./TEST_RESULTS.md)** - Performance measurements

### Contributing & Development
- 🤝 **[Contribution Guidelines](./CONTRIBUTING.md)** - How to contribute code
- 🚀 **[Deployment Guide](./DEPLOYMENT.md)** - Production deployment strategies
- 🔐 **[Security Policy](./SECURITY.md)** - Security considerations and practices

---

## 🛠️ Technology Stack Deep Dive

### Backend Architecture - FastAPI

```python
# Example: How FastAPI validates and documents your APIs
from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI(title="Medical Scribe AI", version="1.0")

# Pydantic model provides:
# 1. Type checking
# 2. JSON schema generation
# 3. Documentation
class LoginRequest(BaseModel):
    email: EmailStr  # Automatic email validation!
    password: str    # Minimum length can be enforced

# FastAPI automatically:
# 1. Validates input JSON
# 2. Converts to Python object
# 3. Generates Swagger documentation
# 4. Shows example values in /docs endpoint
# 5. Returns 422 error if validation fails
@app.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    # request is already validated and typed correctly
    return {"access_token": generate_token(request.email)}
```

### Database Design - SQLAlchemy

```python
# Learning: How ORM maps Python classes to database tables
from sqlalchemy import Column, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    # These Python attributes become database columns
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)  # Index for fast lookups
    hashed_password = Column(String)  # Never store plaintext!
    created_at = Column(DateTime, default=datetime.utcnow)

# Behind the scenes, SQLAlchemy generates SQL:
# CREATE TABLE users (
#     id INTEGER PRIMARY KEY,
#     email VARCHAR NOT NULL UNIQUE,
#     ...
# )

# Python usage:
user = User(email="doctor@clinic.com", hashed_password=bcrypt.hash(pwd))
session.add(user)
session.commit()
# SQLAlchemy generates and executes the SQL INSERT statement
```

### NLP Pipeline - Whisper + Llama2

```python
# The complete workflow:

# Step 1: Load Whisper model (speech-to-text)
import whisper
model = whisper.load_model("base")  # ~140MB model

# Step 2: Transcribe audio
audio = whisper.load_audio("consultation.wav")
result = model.transcribe(audio, language="fr")
transcription = result["text"]  # "Patient reported chest pain..."

# Step 3: Load Llama2 model (text generation)
# Using Ollama to run Llama2 without GPU
import requests
response = requests.post("http://localhost:11434/api/generate", json={
    "model": "llama2",
    "prompt": f"Generate SOAP note from: {transcription}",
    "stream": False
})

soap_note = response.json()["response"]

# Step 4: Extract medical entities
import spacy
nlp = spacy.load("fr_core_news_md")
doc = nlp(transcription)
medications = [ent.text for ent in doc.ents if ent.label_ == "MEDICATION"]
```

---

## 📁 Project Structure & Learning Path

```
Sumy/
│
├── medical-scribe/              # 🏗️ Backend API (Start here for learning)
│   ├── backend/
│   │   └── app/
│   │       ├── main.py          # Application entry point (FastAPI initialization)
│   │       ├── config.py        # Configuration management (environment variables)
│   │       │
│   │       ├── models/          # Database models (SQLAlchemy ORM)
│   │       │   ├── user.py      # User model with JWT integration
│   │       │   ├── recording.py # Audio file metadata
│   │       │   └── medical_note.py # Generated documents
│   │       │
│   │       ├── routers/         # API endpoints (REST routes)
│   │       │   ├── auth.py      # Login/authentication endpoints
│   │       │   ├── recordings.py # Upload and manage audio
│   │       │   ├── transcribe.py # Transcription endpoints
│   │       │   └── notes.py     # Medical note generation
│   │       │
│   │       ├── services/        # Business logic (AI/ML services)
│   │       │   ├── transcription.py # Whisper integration
│   │       │   ├── medical_notes.py # Document generation with Llama2
│   │       │   └── ner.py       # Named Entity Recognition
│   │       │
│   │       └── utils/           # Helper functions
│   │           ├── auth.py      # JWT token handling
│   │           ├── validators.py # Input validation
│   │           └── storage.py   # File management
│   │
│   ├── uploads/                 # Storage for user audio files
│   ├── requirements.txt         # Python dependencies
│   └── start_server.sh         # Startup script
│
├── hypocrate/                   # 🎨 Frontend UI (Streamlit)
│   ├── hypocrate_app.py        # Main Streamlit application
│   ├── config/
│   │   ├── settings.py         # Application settings
│   │   └── prompts.py          # AI prompts for document generation
│   ├── services/
│   │   ├── transcription.py    # Audio processing
│   │   ├── analysis.py         # NER and analysis
│   │   └── generators.py       # SOAP note and letter generation
│   ├── requirements_hypocrate.txt
│   └── start_hypocrate.sh
│
├── docs/                        # 📚 Documentation
│   ├── WINDSURF_2DAY_GUIDE.md   # Training guide
│   ├── QUICK_REFERENCE.md      # Quick lookup
│   └── API.md                  # API reference
│
└── README.md                    # 👈 You are here!

Learning Progression:
1️⃣ Start: Read this README.md
2️⃣ Understand: Review project structure above
3️⃣ Run: Follow Quick Start section
4️⃣ Explore: Review medical-scribe/backend/app/main.py
5️⃣ Experiment: Make API calls using /docs endpoint
6️⃣ Deep Dive: Read services to understand AI integration
7️⃣ Customize: Modify prompts in hypocrate/config/prompts.py
```

---

## 🚦 Development Roadmap

### ✅ Completed (v1.0 - Current)

Core functionality implemented:
- [x] ✅ **Complete RESTful API** with 11 endpoints
- [x] ✅ **JWT-based authentication** for multi-user support
- [x] ✅ **Local Whisper transcription** (no cloud dependencies)
- [x] ✅ **Llama2 integration** for SOAP note generation
- [x] ✅ **Streamlit UI** for direct usage
- [x] ✅ **Medical NER** with scispaCy
- [x] ✅ **Referral letter generation**
- [x] ✅ **Comprehensive documentation**
- [x] ✅ **Security best practices**

### 🔄 In Development (Future v1.1)

Enhancements in progress:
- [ ] **Automated test suite** (unit, integration, end-to-end tests)
- [ ] **Docker containerization** for easy deployment
- [ ] **CI/CD pipeline** (GitHub Actions for automated testing)
- [ ] **Performance monitoring** and logging infrastructure
- [ ] **Database migrations** with Alembic

### 📅 Planned for Future Releases (v2.0+)

Roadmap for future development:
- [ ] **Export Formats**: PDF and DOCX export functionality
- [ ] **Direct Microphone Recording**: Real-time audio capture in Hypocrate
- [ ] **Fine-tuned Models**: Medical-specific Llama2 variants for French language
- [ ] **HL7/FHIR Integration**: Compliance with healthcare data exchange standards
- [ ] **Mobile Applications**: iOS and Android apps
- [ ] **Device Certification**: FDA/CE medical device classification
- [ ] **Advanced Analytics**: Usage reports and outcome tracking
- [ ] **Multi-language Support**: French, Spanish, German, etc.

---

## 🤝 Contributing to This Project

We welcome contributions from developers, doctors, and researchers!

### How to Contribute

**For Developers**:
```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/Sumy.git
cd Sumy

# 3. Create a feature branch
git checkout -b feature/YourFeatureName

# 4. Make your changes
# - Follow Python style guide (PEP 8)
# - Add docstrings to functions
# - Include type hints
# - Write tests for new features

# 5. Test your changes
pytest tests/

# 6. Commit with descriptive message
git commit -m "feat: Add feature description

More detailed explanation if needed.
Fixes: #123  # Reference related issue"

# 7. Push to your fork
git push origin feature/YourFeatureName

# 8. Open a Pull Request on GitHub
# - Describe what changed and why
# - Reference any related issues
# - Ask for review from maintainers
```

### Code Standards

All contributions must follow:

**Python Style**:
- **PEP 8** compliance (use `black` for formatting)
- **Type hints** for all function parameters and returns
- **Docstrings** using Google format (3-line summary, parameters, returns)
- **Logging** instead of print statements for debugging

**Example**:
```python
def generate_soap_note(
    transcription: str,
    patient_age: int,
    special_conditions: Optional[List[str]] = None
) -> dict:
    """
    Generate a SOAP-formatted clinical note from transcription.
    
    This function processes medical consultation transcriptions
    and generates structured SOAP notes (Subjective, Objective,
    Assessment, Plan) suitable for medical records.
    
    Args:
        transcription: Raw text from Whisper transcription
        patient_age: Patient age for context
        special_conditions: List of comorbidities if any
        
    Returns:
        Dictionary containing SOAP note components:
        {
            "subjective": "Patient reports...",
            "objective": "Vitals: BP...",
            "assessment": "Assessment...",
            "plan": "Treatment plan..."
        }
    """
    logger.info(f"Generating SOAP note for {len(transcription)} chars")
    # Implementation...
```

**Testing**:
- **Unit tests** for individual functions
- **Integration tests** for API endpoints
- **Minimum 80% code coverage**
- Tests should be independent and repeatable

### Contribution Areas

**Areas needing help**:

1. **Backend Development**
   - Add new API endpoints
   - Optimize transcription pipeline
   - Enhance error handling
   - Improve database design

2. **Frontend Development**
   - Improve Hypocrate UI/UX
   - Add new visualization types
   - Mobile responsiveness
   - Accessibility features

3. **AI/ML**
   - Fine-tune Llama2 for medical French
   - Improve NER accuracy
   - Add new document types
   - Performance optimization

4. **Documentation**
   - Translate to new languages
   - Create video tutorials
   - Write API documentation
   - Add code examples

5. **Testing & QA**
   - Write comprehensive tests
   - Test across operating systems
   - Performance benchmarking
   - Security testing

---

## 📝 License & Legal

### MIT License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for full details.

**Key points**:
- ✅ Free to use commercially
- ✅ Free to modify
- ✅ Free to distribute
- ✅ Must include original license
- ✅ No warranty provided

### Medical Disclaimer

**⚠️ IMPORTANT: This tool is a clinical decision support aid**

**Limitations**:
- ✅ The clinician remains **legally responsible** for all clinical decisions
- ⚠️ Generated documents **must be reviewed** and verified by a licensed professional
- ⚠️ Does **not replace clinical judgment** or professional training
- ⚠️ Must comply with local medical regulations and professional guidelines
- ⚠️ Not suitable for emergency situations

**Recommended usage**:
1. Use as a **time-saving** documentation tool
2. **Review and validate** all generated content
3. **Modify as needed** to fit specific patient situations
4. **Maintain original records** of actual consultation
5. **Follow institutional guidelines** for medical records

---

## 📞 Support & Troubleshooting

### Common Issues & Solutions

**Issue 1: Ollama not responding**
```bash
# Symptom: "Connection refused" when trying to transcribe

# Solution: Start Ollama service
ollama serve

# Verify Ollama is running
curl http://localhost:11434/api/tags

# Check if Llama2 is installed
ollama list
# If not listed, pull it:
ollama pull llama2
```

**Issue 2: Python version incompatibilities**
```bash
# Symptom: "No module named 'fastapi'" or similar

# Solution: Verify Python version
python3 --version  # Must be 3.10 or higher

# Reinstall dependencies
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

**Issue 3: Port already in use**
```bash
# Symptom: "Address already in use" when starting server

# Solution: Kill process using the port
# For API (port 8001):
lsof -ti:8001 | xargs kill -9

# For Hypocrate (port 8501):
lsof -ti:8501 | xargs kill -9

# Or use different port:
uvicorn backend.app.main:app --port 9001
```

**Issue 4: Audio file not supported**
```bash
# Symptom: "Unsupported audio format"

# Solution: Whisper supports these formats:
# - ✅ WAV (RIFF WAVE)
# - ✅ MP3 (MPEG)
# - ✅ M4A (MPEG-4)
# - ✅ FLAC
# - ✅ OGG

# Convert unsupported formats:
pip install pydub ffmpeg
python -c "
from pydub import AudioSegment
audio = AudioSegment.from_file('input.wav')
audio.export('output.wav', format='wav')
"
```

### Getting Help

**For Bugs & Issues**:
1. Search existing [GitHub Issues](https://github.com/pimvic/Sumy/issues)
2. Open a new issue with:
   - Clear description of problem
   - Steps to reproduce
   - Error messages (full traceback)
   - Your system (OS, Python version, etc.)
   - Log files if applicable

**For Questions & Discussion**:
- Use [GitHub Discussions](https://github.com/pimvic/Sumy/discussions)
- Search documentation first

**For Security Issues**:
- Do NOT open public issues
- Email: security@sumy.ai (or check SECURITY.md)
- Privately disclose vulnerability

---

## 🙏 Acknowledgments

### Open Source Projects

This project builds on these excellent open-source tools:

- **[OpenAI Whisper](https://github.com/openai/whisper)** - Speech-to-text AI
  - Enables local transcription without API calls
  - Supports 99 languages

- **[Ollama](https://ollama.ai/)** - Local LLM Runtime
  - Makes running large language models accessible on consumer hardware
  - Provides simple API for model inference

- **[Meta Llama2](https://ai.meta.com/llama/)** - Open Large Language Model
  - Trained on diverse datasets
  - Free for research and commercial use

- **[scispaCy](https://allenai.github.io/scispacy/)** - Biomedical NLP
  - Pre-trained on medical literature
  - Efficient named entity recognition for clinical text

- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern Python Web Framework
  - Type hints and auto-documentation
  - High performance and easy to learn

- **[Streamlit](https://streamlit.io/)** - Rapid Web App Development
  - Python-only development (no JavaScript needed)
  - Perfect for data science applications

---

## 🌟 Star This Project!

If you find this project useful for learning, research, or clinical practice, please consider giving it a ⭐️ on GitHub!

Your stars help:
- ✅ Increase visibility in the community
- ✅ Attract more contributors
- ✅ Support continued development
- ✅ Help other developers find the project

---

## 🚀 Next Steps

### For Learning Developers

1. **Understand the Architecture** (30 min)
   - Read the Architecture section above
   - Review the project structure
   - Look at medical-scribe/backend/app/main.py

2. **Run the Application** (15 min)
   - Follow Quick Start section
   - Test API endpoints using /docs
   - Try Hypocrate web interface

3. **Explore the Code** (1-2 hours)
   - Review service files for AI integration
   - Understand database models
   - Check authentication mechanisms

4. **Modify & Extend** (varies)
   - Adjust prompts in config files
   - Add new API endpoints
   - Create custom document types

### For Medical Professionals

1. **Try the Interface** (10 min)
   - Start Hypocrate UI
   - Upload a test audio file
   - Review generated documents

2. **Integrate into Workflow** (varies)
   - Connect to your existing systems
   - Test with real consultations
   - Measure time savings

3. **Provide Feedback**
   - Report issues on GitHub
   - Suggest improvements
   - Share your experience

---

<div align="center">

## 🏥 Medical Scribe AI - Sumy

**Transforming Medical Documentation with Open-Source AI**

*Built for learning, designed for privacy, optimized for healthcare*

### 📚 Documentation

[Quick Start](./medical-scribe/QUICKSTART.md) • 
[API Guide](./medical-scribe/README.md) • 
[Hypocrate Guide](./hypocrate/README.md) • 
[Full Documentation](./PROJET_COMPLET.md)

### 🔗 Resources

[GitHub Repository](https://github.com/pimvic/Sumy) • 
[Issues & Discussions](https://github.com/pimvic/Sumy/issues) • 
[Contributing Guide](./CONTRIBUTING.md) • 
[Security Policy](./SECURITY.md)

### 📄 License

Licensed under MIT - See [LICENSE](LICENSE) for details

---

*Made with ❤️ for healthcare professionals and developers* 🏥
*Contributions welcome! Fork, modify, and share improvements* 🚀

</div>

````