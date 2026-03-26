# Medical Scribe AI - Quick Start Guide (English)

## 🚀 Get Started in 10 Minutes

This guide will help you set up and run the Medical Scribe API backend on your local machine. We'll walk through authentication, API testing, and system setup.

### 📋 Prerequisites

Before you start, make sure you have:

```bash
# Check Python version (must be 3.10+ for type hints feature)
python3 --version
# Output should show: Python 3.10.x or higher

# Check pip is available
python3 -m pip --version

# Check git is installed
git --version

# Ensure Ollama is running (for AI models)
ollama serve &
```

---

## ⚙️ Step 1: Environment Setup (2 minutes)

The environment setup configures your application with necessary secrets and configuration variables.

```bash
# Navigate to the project
cd Sumy/medical-scribe

# Run the setup script (creates .env with SECRET_KEY)
./setup_env.sh

# What setup_env.sh does:
# 1. Creates .env file with random SECRET_KEY
# 2. Sets SQLALCHEMY_DATABASE_URL
# 3. Initializes default configuration
# 4. Creates uploads directory for audio files
```

### Understanding the `.env` File

The `.env` file stores sensitive configuration. Never commit it to Git!

```bash
# View your .env
cat .env

# Example .env contents:
# SECRET_KEY=your-secret-key-generated-here (DO NOT SHARE!)
# DATABASE_URL=sqlite:///./medical_scribe.db
# OLLAMA_HOST=http://localhost:11434 (Local LLM)
# DEBUG=False

# If you need to edit it:
nano .env  # or your preferred text editor
```

### Key Configuration Details

| Variable | Purpose | Security Note |
|----------|---------|---------------|
| `SECRET_KEY` | Encrypts JWT tokens and session data | ⚠️ Never share! Keep private |
| `DATABASE_URL` | SQLite database connection string | Local file, auto-created |
| `OLLAMA_HOST` | Local LLM server address | Default: localhost:11434 |
| `DEBUG` | Enable debug mode (never in production!) | ⚠️ Only for development |

---

## 🔧 Step 2: Install Dependencies (3 minutes)

Python dependencies are specified in `requirements.txt`. Dependencies are:
- Exact versions to ensure reproducibility
- Tested together to ensure compatibility
- Organized by category (web, database, AI, utility)

```bash
# Create virtual environment (isolates dependencies for this project)
python3 -m venv venv

# Activate virtual environment
# macOS/Linux:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# Verify you're in the virtual environment (should show (venv) prefix)
which python3  # Should point to venv/bin/python3

# Upgrade pip to latest version (prevents installation issues)
python3 -m pip install --upgrade pip

# Install all dependencies from requirements.txt
pip install -r requirements.txt

# What gets installed:
# - fastapi (web framework)
# - sqlalchemy (database ORM)
# - pydantic (data validation)
# - python-jose (JWT tokens)
# - bcrypt (password hashing)
# - python-multipart (file uploads)
# - openai-whisper (speech recognition - ~500MB)
# - requests (HTTP client for Ollama)
```

### Troubleshooting Dependencies

```bash
# If installation fails, try:

# 1. Clear pip cache
pip cache purge

# 2. Reinstall with verbose output
pip install -r requirements.txt -v

# 3. Check for conflicting packages
pip check

# 4. Install one by one to identify problematic package
pip install fastapi sqlalchemy pydantic ...
```

---

## 🚀 Step 3: Start the Backend Server (1 minute)

The FastAPI development server provides auto-reload, which means the server automatically restarts when you modify code files.

```bash
# Make sure you're in the virtual environment
# (your terminal should show (venv) prefix)

# Change to the medical-scribe directory
cd /path/to/Sumy/medical-scribe

# Start the server  (runs on port 8001)
python -m uvicorn backend.app.main:app --reload --port 8001

# Expected output:
# INFO:     Uvicorn running on http://0.0.0.0:8001
# INFO:     Application startup complete
```

### Understanding Server Output

```
INFO:     Uvicorn running on http://0.0.0.0:8001
# The server is listening on all network interfaces

INFO:     Application startup complete
# All startup events have completed successfully

INFO:     Shutting down gracefully...
# Server is shutting down (happens when you press Ctrl+C)
```

### Server Options Explained

| Option | Purpose | When to Use |
|--------|---------|-----------|
| `--reload` | Auto-restart on code changes | Development only (slower) |
| `--port 8001` | Server port (default is 8000) | Avoid port conflicts |
| `--host 0.0.0.0` | Listen on all network interfaces | For remote access |
| `--workers 4` | Number of worker processes | Production (multi-core) |

### Keep Server Running

Once started, leave the server running in a terminal window. Open a new terminal for the next steps:

```bash
# Terminal 1 (leave this running):
cd Sumy/medical-scribe
python -m uvicorn backend.app.main:app --reload --port 8001

# Terminal 2 (use this for testing):
# Open a new terminal window and run test commands below
```

---

## 🧪 Step 4: Test the API (4 minutes)

Now that the server is running, let's test it with actual API calls. There are three ways to test:

### Option A: Interactive Swagger Documentation (Recommended for Beginners)

The `/docs` endpoint provides an interactive interface where you can test all API endpoints directly from your browser.

```
Browser URL: http://localhost:8001/docs
```

**Features**:
- ✅ See all available endpoints
- ✅ View request/response schemas
- ✅ Test endpoints directly from browser
- ✅ Auto-generated from your Python code

**Step-by-step**:
1. Open http://localhost:8001/docs in your browser
2. Look for "POST /api/auth/register" endpoint
3. Click on it to expand
4. Click "Try it out" button
5. Fill in the test data below
6. Click "Execute"

###Option B: ReDoc Alternative Documentation

An alternative documentation format (read-only, good for documentation):

```
Browser URL: http://localhost:8001/redoc
```

### Option C: Command Line using cURL

Use curl commands for scripting and automation:

```bash
# ============================================
# 1️⃣ CREATE AN ACCOUNT (REGISTER)
# ============================================

curl -X POST http://localhost:8001/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "doctor@clinic.com",
    "password": "SecurePassword123!",
    "full_name": "Dr. John Smith"
  }'

# Expected response (201 Created):
# {
#   "id": 1,
#   "email": "doctor@clinic.com",
#   "full_name": "Dr. John Smith",
#   "created_at": "2024-03-26T12:00:00"
# }

# ============================================
# 2️⃣ AUTHENTICATE (LOGIN)
# ============================================

curl -X POST http://localhost:8001/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "doctor@clinic.com",
    "password": "SecurePassword123!"
  }'

# Expected response (200 OK):
# {
#   "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
#   "token_type": "bearer"
# }

# IMPORTANT: Copy the entire access_token value
# YOU'LL NEED THIS FOR ALL OTHER REQUESTS

# ============================================
# 3️⃣ GET AUTHENTICATED USER INFO
# ============================================

# Replace YOUR_ACCESS_TOKEN with the token from step 2
curl -X GET http://localhost:8001/api/auth/me \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# Expected response (200 OK):
# {
#   "id": 1,
#   "email": "doctor@clinic.com",
#   "full_name": "Dr. John Smith",
#   "created_at": "2024-03-26T12:00:00"
# }

# ============================================
# 4️⃣ UPLOAD AN AUDIO FILE
# ============================================

# First, find an audio file or create a test one:
# - Download from internet, or
# - Use system sounds, or
# - Record one from terminal:
# ffmpeg -f avfoundation -i ":0" -t 5 test_audio.wav

curl -X POST http://localhost:8001/api/recordings/upload \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -F "file=@/path/to/audio.wav"

# Expected response (200 OK):
# {
#   "id": 1,
#   "filename": "audio.wav",
#   "duration": 125.5,
#   "status": "uploaded",
#   "created_at": "2024-03-26T12:00:00"
# }

# ============================================
# 5️⃣ TRANSCRIBE THE AUDIO
# ============================================

# Use the recording ID from step 4
curl -X POST http://localhost:8001/api/recordings/1/transcribe \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# This might take a minute or two...
# Expected response (200 OK):
# {
#   "id": 1,
#   "transcription": "Patient reports chest pain starting yesterday afternoon...",
#   "status": "completed",
#   "processing_time": 45.2
# }

# ============================================
# 6️⃣ GENERATE MEDICAL NOTES
# ============================================

curl -X POST http://localhost:8001/api/recordings/1/generate_medical_notes \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "note_type": "soap"
  }'

# Expected response (200 OK):
# {
#   "id": 1,
#   "soap_note": {
#     "subjective": "Patient reports chest pain...",
#     "objective": "Vitals: BP 140/90, HR 88...",
#     "assessment": "Acute chest pain, likely musculoskeletal...",
#     "plan": "Rest, NSAIDs, follow up in 1 week..."
#   },
#   "processing_time": 32.1
# }
```

### Understanding Responses

All API responses follow a standard format:

```json
{
  "status": 200,      // HTTP status code
  "data": { ... },    // Actual response data
  "message": "Success", // Human-readable message
  "timestamp": "2024-03-26T12:00:00" // When response was generated
}
```

---

## ✅ Verify Setup is Complete

After completing the steps above, you should see:

```
✅ Environment configured (.env file created)
✅ Dependencies installed (pip install completed)
✅ Server running (http://localhost:8001 accessible)
✅ Database initialized (SQLite file created)
✅ Can create user (registration endpoint works)
✅ Can authenticate (login returns JWT token)
✅ Can upload files (audio files accepted)
✅ Can process audio (transcription working)
✅ Can generate documents (SOAP notes generated)
```

---

## 📚 API Endpoints Reference

### Authentication Endpoints

| Method | Endpoint | Purpose | Auth Required |
|--------|----------|---------|----------------|
| POST | `/api/auth/register` | Create new user account | No |
| POST | `/api/auth/login` | Login and get JWT token | No (uses credentials) |
| GET | `/api/auth/me` | Get current user info | Yes |
| POST | `/api/auth/logout` | Logout (invalidate token) | Yes |
| POST | `/api/auth/refresh` | Refresh JWT token | Yes |

### Recording Endpoints

| Method | Endpoint | Purpose | Auth Required |
|--------|----------|---------|----------------|
| POST | `/api/recordings/upload` | Upload audio file | Yes |
| GET | `/api/recordings` | List all recordings | Yes |
| GET | `/api/recordings/{id}` | Get recording details | Yes |
| DELETE | `/api/recordings/{id}` | Delete recording | Yes |

### Processing Endpoints

| Method | Endpoint | Purpose | Auth Required |
|--------|----------|---------|----------------|
| POST | `/api/recordings/{id}/transcribe` | Transcribe audio | Yes |
| POST | `/api/recordings/{id}/generate_medical_notes` | Generate SOAP note | Yes |
| GET | `/api/recordings/{id}/status` | Check processing status | Yes |

### Documentation Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/docs` | Interactive Swagger UI |
| GET | `/redoc` | ReDoc documentation |
| GET | `/openapi.json` | OpenAPI schema (JSON) |

---

## 🎯 Next Steps After Setup

### 1. Explore the Code (20 minutes)

Review these files to understand the architecture:

```python
# backend/app/main.py
# - FastAPI app initialization
# - Startup/shutdown events
# - CORS configuration
# - Database initialization

# backend/app/models/
# - user.py: User database model
# - recording.py: Audio file metadata
# - medical_note.py: Generated documents

# backend/app/routers/
# - auth.py: Authentication endpoints
# - recordings.py: File management endpoints
# - transcribe.py: Transcription endpoints

# backend/app/services/
# - transcription.py: Whisper integration
# - medical_notes.py: Document generation
# - ner.py: Named entity recognition
```

### 2. Customize Configuration

Edit settings to match your needs:

```bash
# .env file - change these:
SECRET_KEY=your-secret-here (already set, leave it)
DATABASE_URL=sqlite:///./medical_scribe.db (can change path)
OLLAMA_HOST=http://localhost:11434 (if running elsewhere)
DEBUG=False (set to True for development)
```

### 3. Run the Hypocrate UI

After the API is working, try the web interface:

```bash
cd Sumy/hypocrate
python -m streamlit run hypocrate_app.py --server.port 8501

# Open: http://localhost:8501
```

### 4. Read Full Documentation

For deeper understanding, read:

- [Complete Architecture Guide](./PROJET_COMPLET.md)
- [Deployment Guide](./DEPLOYMENT.md)
- [Security Best Practices](./SECURITY.md)
- [Contributing Guidelines](./CONTRIBUTING.md)

---

## 🆘 Troubleshooting

### Issue: "ValidationError: OLLAMA_HOST Field required"

**Problem**: Ollama isn't configured properly

**Solution**:
```bash
# 1. Ensure Ollama is running
ollama serve

# 2. Test Ollama connection
curl http://localhost:11434/api/tags

# 3. Check .env file has correct OLLAMA_HOST
cat .env | grep OLLAMA_HOST
```

### Issue: "ModuleNotFoundError: No module named 'fastapi'"

**Problem**: Dependencies aren't installed

**Solution**:
```bash
# Activate virtual environment
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt

# Verify (should show FastAPI version)
pip show fastapi
```

### Issue: "Address already in use: ('0.0.0.0', 8001)"

**Problem**: Port 8001 is already in use

**Solution**:
```bash
# Find what's using the port
lsof -ti:8001

# Kill it (replace PID with actual process ID)
kill -9 <PID>

# OR use a different port
python -m uvicorn backend.app.main:app --port 8002
```

### Issue: "jwt.exceptions.DecodeError" when accessing protected endpoints

**Problem**: Invalid or expired JWT token

**Solution**:
```bash
# 1. Get a new token by logging in again
curl -X POST http://localhost:8001/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "doctor@clinic.com", "password": "password"}'

# 2. Use the new token in Authorization header
curl -H "Authorization: Bearer NEW_TOKEN" ...
```

### Issue: Whisper model takes forever to download

**Problem**: First-time Whisper usage downloads large model (~2.5GB)

**Solution**:
```bash
# Pre-download the model:
python -c "import whisper; whisper.load_model('base')"

# Subsequent uses will be instant

# For faster but less accurate model:
python -c "import whisper; whisper.load_model('tiny')"
```

---

## 📖 Understanding the API Flow

Here's a complete workflow from start to finish:

```
┌─────────────────────────────────────────────────────┐
│ 1. USER REGISTRATION                                │
│ POST /api/auth/register                             │
│ {email, password, full_name}                        │
│ → Creates user in database (password hashed)        │
└─────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────┐
│ 2. USER AUTHENTICATION                              │
│ POST /api/auth/login                                │
│ {email, password}                                   │
│ → Returns JWT token valid for 24 hours              │
└─────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────┐
│ 3. AUTHENTICATED OPERATIONS                         │
│ All subsequent requests include: Authorization: Bearer TOKEN  │
│                                                      │
│ 3a. Upload Recording                                │
│     POST /api/recordings/upload                     │
│     → Validates file, saves to disk                 │
│                                                      │
│ 3b. Transcribe Audio                                │
│     POST /api/recordings/{id}/transcribe            │
│     → Loads Whisper model, processes audio          │
│     → Stores transcription in database              │
│                                                      │
│ 3c. Generate Medical Notes                          │
│     POST /api/recordings/{id}/generate_medical_notes│
│     → Takes transcription + prompt                  │
│     → Calls Llama2 for generation                   │
│     → Stores SOAP note in database                  │
└─────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────┐
│ 4. RETRIEVE RESULTS                                 │
│ GET /api/recordings/{id}                            │
│ → Returns all data: transcription + notes + metadata│
└─────────────────────────────────────────────────────┘
```

---

## 💡 Learning Tips

### Debugging API Issues

```bash
# Enable verbose output to see HTTP details
curl -v -X GET http://localhost:8001/api/auth/me \
  -H "Authorization: Bearer TOKEN"

# Shows:
# > GET /api/auth/me HTTP/1.1  (request line)
# > Authorization: Bearer ...  (request headers)
# < HTTP/1.1 200 OK             (response status)
# < content-type: application/json (response headers)
```

### Exploring the Database

```bash
# View SQLite database
sqlite3 medical_scribe.db

# Show all tables
.tables

# View users
SELECT id, email, created_at FROM user;

# View recordings
SELECT id, filename, duration, status FROM recording;

# Exit
.quit
```

### Reading API Errors

All API errors follow this format:

```json
{
  "detail": "User not found",  // Error message
  "status": 404               // HTTP status code
}
```

Common status codes:
- `200 OK` - Request succeeded
- `201 Created` - Resource created
- `400 Bad Request` - Invalid input
- `401 Unauthorized` - Missing/invalid token
- `404 Not Found` - Resource doesn't exist
- `500 Server Error` - Internal server error

---

## 🎓 Key Learning Concepts

### JWT Authentication

```python
# When you login, you receive a JWT token:
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.
# eyJzdWIiOjEsImV4cCI6MTcxMTQ0MDAwMH0.
# signature...

# This token contains:
# 1. Header: Algorithm (HS256)
# 2. Payload: user_id, expiration time (encoded, not encrypted)
# 3. Signature: Proves token wasn't tampered with

# Server trusts the token because:
# - IT created the signature with SECRET_KEY
# - Only the server knows SECRET_KEY
# - If payload was modified, signature won't match
```

### REST API Principles

```python
# Resources: /api/auth, /api/recordings
# HTTP Methods:
#   GET    - Retrieve data (safe, idempotent)
#   POST   - Create new data (not idempotent)
#   PUT    - Update entire resource
#   PATCH  - Update part of resource
#   DELETE - Remove resource

# Status Codes:
#   2xx - Success
#   4xx - Client error (bad request)
#   5xx - Server error (our fault)
```

### Database Design

```python
# Each Table represents a entity:
# - users: Stores user accounts
# - recordings: Stores audio file metadata
# - medical_notes: Stores generated documents

# Relationships:
# - One User has Many Recordings
# - One Recording has One Medical Note
# - Foreign Keys maintain referential integrity
```

---

<div align="center">

## 🎉 You're Ready!

Your Medical Scribe API is now running and ready for:
- ✅ Development and testing
- ✅ Backend integration
- ✅ Custom application building
- ✅ Production deployment

### Need Help?

- 📚 [Full Documentation](./PROJET_COMPLET.md)
- 🐛 [Report Issues](https://github.com/pimvic/Sumy/issues)
- 💬 [Discussions](https://github.com/pimvic/Sumy/discussions)

### Ready for Frontend?

Try the Hypocrate web interface:
```bash
cd ../hypocrate
python -m streamlit run hypocrate_app.py
```

---

*Happy coding! 🚀*

</div>

````