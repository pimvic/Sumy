# 🚀 Medical Scribe AI - Deployment Guide (English)

## Table of Contents

1. [Deployment Strategies](#deployment-strategies) - Learn different deployment approaches
2. [Local Development Setup](#local-development-setup) - Setup for development
3. [Docker Containerization](#docker-containerization) - Container-based deployment
4. [Production Deployment](#production-deployment) - Enterprise-grade setup
5. [Scaling & Performance](#scaling--performance) - Handling multiple users
6. [Monitoring & Logging](#monitoring--logging) - System health tracking
7. [Troubleshooting](#troubleshooting) - Common issues and fixes

---

## 🎯 Deployment Strategies

### Overview of Deployment Options

| Deployment Type | Complexity | Scalability | Cost | Best For |
|-----------------|-----------|-----------|------|---------|
| **Local Development** | ⭐ Easy | Single User | Free | Learning, Testing |
| **Docker Compose** | ⭐⭐ Medium | Small Team | Low | Small clinics |
| **Kubernetes** | ⭐⭐⭐ Advanced | Enterprise | Medium | Large hospitals |
| **Cloud (AWS/GCP)** | ⭐⭐ Medium | Unlimited | Variable | Global reach |

### Deployment Decision Tree

```
Start Here: Where will you run the application?
    │
    ├─ Own computer? → Local Development Setup
    │
    ├─ Single clinic/office? → Docker Compose
    │
    ├─ Multiple locations? → Cloud Deployment
    │
    └─ Large organization? → Kubernetes + Cloud
```

---

## 💻 Local Development Setup

### Phase 1: Prerequisites Installation (10 minutes)

Before deploying locally, ensure your system has necessary software:

```bash
# Check Python version (must be 3.10+)
python3 --version

# Install Ollama (provides local LLM service)
# macOS:
brew install ollama

# Linux:
curl https://ollama.ai/install.sh | sh

# Windows:
# Download from https://ollama.ai/download

# Verify Ollama installation
ollama --version

# Pull Llama2 model (7B version, ~4GB download)
ollama pull llama2

# This enables local text generation without API calls
```

### Phase 2: Medical Scribe API Deployment

```bash
# Step 1: Navigate to project
git clone https://github.com/pimvic/Sumy.git
cd Sumy/medical-scribe

# Step 2: Create Python virtual environment
# (isolates dependencies from system Python)
python3 -m venv venv

# Step 3: Activate virtual environment
source venv/bin/activate  # macOS/Linux

# OR on Windows:
# venv\Scripts\activate

# You should see (venv) prefix in terminal

# Step 4: Upgrade pip
python -m pip install --upgrade pip

# Step 5: Install dependencies
pip install -r requirements.txt

# This installs:
# - fastapi (web framework)
# - sqlalchemy (database ORM)
# - python-multipart (file upload handling)
# - openai-whisper (speech recognition)
# - python-jose + bcrypt (security)
# - pydantic (data validation)
# - uvicorn (ASGI server)

# Step 6: Initialize environment
./setup_env.sh

# This creates:
# - .env file with configuration
# - uploads/ directory for audio files
# - SQLite database file (auto-created on first run)

# Step 7: Start the server
./start_server.sh
```

**Expected Output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8001
INFO:     Application startup complete
```

**Verify Deployment:**
```bash
# Open in browser:
http://localhost:8001/docs

# Or test with curl:
curl http://localhost:8001/docs
```

### Phase 3: Hypocrate UI Deployment

```bash
# From medical-scribe parent directory
cd ../hypocrate

# Use same virtual environment OR create new one
# (recommended to use same for shared dependencies)
source ../medical-scribe/venv/bin/activate

# Install frontend-specific dependencies
pip install -r requirements_hypocrate.txt

# Download NLP models for text processing
# French medical text processing
python -m spacy download fr_core_news_md

# English support (for some documents)
python -m spacy download en_core_web_sm

# Install scispaCy (biomedical NLP)
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.0/en_ner_bc5cdr_md-0.5.0.tar.gz

# Start Hypocrate
./start_hypocrate.sh
```

**Access Hypocrate:**
```
Open in browser: http://localhost:8501
```

---

## 🐳 Docker Containerization

###What is Docker?

Docker creates **lightweight, portable containers** that bundle your application with all dependencies. Benefits:

- ✅ **Consistency**: Same environment across dev, test, production
- ✅ **Isolation**: Application doesn't interfere with system
- ✅ **Scalability**: Easy to run multiple instances
- ✅ **Deployment**: One command to deploy anywhere

### Installing Docker

```bash
# macOS:
brew install docker docker-compose

# Linux (Ubuntu/Debian):
sudo apt-get update
sudo apt-get install docker.io docker-compose

# Windows:
# Download Docker Desktop from https://docker.com/products/docker-desktop

# Verify installation:
docker --version
docker-compose --version
```

### Dockerfile for Medical Scribe API

Create `medical-scribe/Dockerfile`:

```dockerfile
# Use lightweight Python image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Install system dependencies required by Python packages
# - ffmpeg: Audio format conversion (required by Whisper)
# - libsndfile1: Audio file library
# - libgomp1: OpenMP library (required by some libraries)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    libgomp1 \
    curl \
    && rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size

# Copy Python dependencies file
COPY requirements.txt .

# Install Python dependencies
# --no-cache-dir reduces image size by not storing pip cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY backend/ ./backend/

# Create uploads directory for audio files
RUN mkdir -p ./uploads

# Set environment variables
ENV PYTHONUNBUFFERED=1 (output logs immediately)
ENV DATABASE_URL=sqlite:///./medical_scribe.db

# Expose port
EXPOSE 8001

# Health check (Docker checks if app is still running)
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8001/docs || exit 1

# Start command
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8001"]
```

### Docker Compose Configuration

Create `docker-compose.yml` at project root:

```yaml
version: '3.8'  # Docker Compose format version

services:
  # ============================================
  # API Service (Medical Scribe)
  # ============================================
  api:
    # Build from Dockerfile
    build:
      context: ./medical-scribe
      dockerfile: Dockerfile
    
    # Port mapping (host:container)
    ports:
      - "8001:8001"  # API runs on 8001
    
    # Mount volumes (persistent storage)
    volumes:
      # Upload directory (persists audio files)
      - ./medical-scribe/uploads:/app/uploads
      # Database file (persists user data)
      - ./medical-scribe/medical_scribe.db:/app/medical_scribe.db
    
    # Environment configuration
    environment:
      - DATABASE_URL=sqlite:///./medical_scribe.db
      - OLLAMA_HOST=http://ollama:11434  # For Ollama container
      - USE_LOCAL_MODELS=true
      - DEBUG=False
    
    # Start after dependencies
    depends_on:
      - ollama
    
    # Network for inter-container communication
    networks:
      - scribemed-network
    
    # Automatically restart if container stops
    restart: unless-stopped
    
    # Limit resource usage
    deploy:
      resources:
        limits:
          cpus: '2'      # Max 2 CPU cores
          memory: 4G     # Max 4GB RAM
        reservations:
          cpus: '0.5'    # Reserve 0.5 cores
          memory: 2G     # Reserve 2GB RAM

  # ============================================
  # Ollama Service (Local LLM)
  # ============================================
  ollama:
    # Official Ollama image
    image: ollama/ollama:latest
    
    # Port mapping
    ports:
      - "11434:11434"  # Ollama API
    
    # Volume for model storage (persists downloaded models)
    volumes:
      - ollama_data:/root/.ollama
    
    # Network access
    networks:
      - scribemed-network
    
    # Resource limits (LLMs are memory-intensive)
    deploy:
      resources:
        limits:
          cpus: '4'
          memory: 16G
    
    restart: unless-stopped
    
    # Set GPU (if available)
    # (Uncomment if you have NVIDIA GPU)
    # runtime: nvidia

  # ============================================
  # Hypocrate Service (Web UI)
  # ============================================
  hypocrate:
    build:
      context: ./hypocrate
      dockerfile: Dockerfile
    
    ports:
      - "8501:8501"  # Streamlit runs on 8501
    
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - OLLAMA_HOST=http://ollama:11434
      - API_URL=http://api:8001
    
    depends_on:
      - api
      - ollama
    
    networks:
      - scribemed-network
    
    restart: unless-stopped
    
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G

# ============================================
# Volumes (Persistent Storage)
# ============================================
volumes:
  # Ollama models storage
  ollama_data:
    driver: local
  
  # Optional: Database backup
  db_backup:
    driver: local

# ============================================
# Networks (Inter-container Communication)
# ============================================
networks:
  scribemed-network:
    driver: bridge
```

### Building and Running with Docker

```bash
# Build all service images
docker-compose build

# Start all services
docker-compose up

# Start in background
docker-compose up -d

# View running containers
docker-compose ps

# View logs
docker-compose logs -f  # Follow logs in real-time
docker-compose logs api # API logs only

# Stop services
docker-compose down

# Remove everything (including data!)
docker-compose down -v

# Rebuild specific service
docker-compose build api
docker-compose up api
```

### Verifying Docker Deployment

```bash
# Check if containers are running
docker-compose ps

# Test API
curl http://localhost:8001/docs

# Test Ollama connection
curl http://localhost:11434/api/tags

# Enter a running container
docker-compose exec api bash

# View container logs
docker-compose logs api --tail 100
```

---

## 🏢 Production Deployment

### Production Architecture

For healthcare systems, recommend this architecture:

```
┌─────────────────────────────────────────────────┐
│           Load Balancer (Nginx)                 │
│  (Distributes traffic across multiple servers)  │
└────────────┬────────────────────────────────────┘
             │
      ┌──────┴────────┬─────────────┐
      ▼               ▼             ▼
┌──────────┐  ┌──────────┐  ┌──────────┐
│  API #1  │  │  API #2  │  │  API #3  │
│ Port 8001│  │ Port 8001│  │ Port 8001│
└─────┬────┘  └─────┬────┘  └─────┬────┘
      │             │             │
      └─────────────┼─────────────┘
                    │
         ┌──────────┴──────────┐
         ▼                     ▼
    ┌─────────┐         ┌─────────┐
    │ Database│         │  Cache  │
    │(PostgreSQL)       │(Redis)  │
    └─────────┘         └─────────┘
```

### Production Systemd Service

Create `/etc/systemd/system/scribemed-api.service`:

```ini
[Unit]
Description=Medical Scribe AI Backend API
After=network.target

[Service]
Type=notify
User=scribemed
WorkingDirectory=/opt/scribemed/api

# Python virtual environment
Environment="PATH=/opt/scribemed/api/venv/bin"

# Increase file descriptor limit (for many concurrent users)
LimitNOFILE=65536

# Restart policy
Restart=on-failure
RestartSec=5s

# Kill signal (graceful shutdown)
KillMode=mixed
KillSignal=SIGQUIT

# Start command
ExecStart=/opt/scribemed/api/venv/bin/uvicorn \
    backend.app.main:app \
    --host 0.0.0.0 \
    --port 8001 \
    --workers 4 \
    --worker-class uvicorn.workers.UvicornWorker

[Install]
WantedBy=multi-user.target
```

### Starting Service

```bash
# Enable service (start on boot)
sudo systemctl enable scribemed-api.service

# Start service
sudo systemctl start scribemed-api.service

# Check status
sudo systemctl status scribemed-api.service

# View logs
sudo journalctl -u scribemed-api.service -f

# Stop service
sudo systemctl stop scribemed-api.service
```

### Nginx Reverse Proxy Configuration

Create `/etc/nginx/sites-available/scribemed`:

```nginx
upstream scribemed_api {
    # Define backend servers (load balancing)
    server localhost:8001 max_fails=3 fail_timeout=30s;
    server localhost:8002 max_fails=3 fail_timeout=30s;
    server localhost:8003 max_fails=3 fail_timeout=30s;
}

server {
    # Listening configuration
    listen 80;
    listen [::]:80;
    server_name api.scribemed.local;

    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    # HTTPS configuration
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name api.scribemed.local;

    # SSL certificates
    ssl_certificate /etc/letsencrypt/live/scribemed.local/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/scribemed.local/privkey.pem;

    # Security headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "DENY" always;
    add_header X-XSS-Protection "1; mode=block" always;

    # Compression
    gzip on;
    gzip_types application/json;
    gzip_min_length 1000;

    # Proxy to backend
    location / {
        proxy_pass http://scribemed_api;
        
        # Forward headers
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Timeouts
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
        
        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    # API documentation (keep public)
    location /docs {
        proxy_pass http://scribemed_api;
    }

    # Health check endpoint
    location /health {
        proxy_pass http://scribemed_api;
        access_log off;
    }
}
```

---

## 📊 Scaling & Performance

### Horizontal Scaling (Multiple Servers)

```bash
# Start API on multiple ports
uvicorn backend.app.main:app --port 8001 &
uvicorn backend.app.main:app --port 8002 &
uvicorn backend.app.main:app --port 8003 &

# Nginx distributes traffic across all
# If one fails, others continue serving requests
```

### Database Optimization for Scale

```python
# For large deployments, migrate to PostgreSQL:

# In .env:
DATABASE_URL=postgresql://user:password@localhost/scribemed

# Benefits over SQLite:
# - Multiple concurrent connections (SQLite limited)
# - Full-text search capabilities
# - Replication support
# - Better indexing options
```

### Caching Strategy

```python
# Use Redis to cache frequently accessed data

from redis import Redis

cache = Redis(host='localhost', port=6379)

@app.get("/recordings/{id}")
async def get_recording(id: int):
    # Check cache first
    cached = cache.get(f"recording:{id}")
    if cached:
        return json.loads(cached)  # Return from cache
    
    # Otherwise get from database
    recording = db.query(Recording).filter(Recording.id == id).first()
    
    # Store in cache for 1 hour
    cache.setex(f"recording:{id}", 3600, json.dumps(recording))
    
    return recording
```

---

## 📊 Monitoring & Logging

### Application Monitoring

```python
# Add monitoring middleware to FastAPI

from prometheus_client import Counter, Histogram
import time

# Metrics
request_count = Counter(
    'api_requests_total',
    'Total API requests',
    ['method', 'endpoint']
)

request_duration = Histogram(
    'api_request_duration_seconds',
    'API request duration',
    ['method']
)

@app.middleware("http")
async def add_metrics(request: Request, call_next):
    start_time = time.time()
    
    response = await call_next(request)
    
    # Record metrics
    duration = time.time() - start_time
    request_count.labels(
        method=request.method,
        endpoint=request.url.path
    ).inc()
    request_duration.labels(method=request.method).observe(duration)
    
    return response
```

### Logging Configuration

```python
# In backend/app/main.py

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

@app.on_event("startup")
async def startup():
    logger.info("Application startup")
    logger.info(f"Database: {settings.database_url}")

@app.post("/api/auth/login")
async def login(credentials: LoginRequest):
    logger.info(f"Login attempt: {credentials.email}")
    try:
        user = authenticate_user(credentials)
        logger.info(f"Login success: {credentials.email}")
    except Exception as e:
        logger.error(f"Login failed: {str(e)}")
        raise
```

---

## 🔧 Troubleshooting

### Issue: "Connection refused" when accessing http://localhost:8001

```bash
# Check if API is running
ps aux | grep uvicorn

# Check if port is listening
netstat -an | grep 8001
# or
lsof -i :8001

# Try starting server manually
cd medical-scribe
python -m uvicorn backend.app.main:app --port 8001
```

### Issue: Docker container exits immediately

```bash
# Check container logs
docker-compose logs api

# Rebuild container
docker-compose down
docker-compose build --no-cache api
docker-compose up api

# Test manually
docker run -it scribemed-api bash
python -m uvicorn backend.app.main:app
```

### Issue: Out of memory when running models

```bash
# Check available memory
python -c "import psutil; print(f'Available: {psutil.virtual_memory().available / 1024**3:.1f}GB')"

# Use smaller models
# In your code:
model = whisper.load_model("tiny")  # 1GB instead of 2.5GB
# or
model = whisper.load_model("base")  # 1.5GB

# Allocate more swap (temporary fix)
fallocate -l 4G /swapfile
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
```

### Issue: Database locked (SQLite)

```bash
# Remove stale locks
rm -f ./medical_scribe.db-wal
rm -f ./medical_scribe.db-shm

# Migrate to PostgreSQL for production
# SQLite not suitable for multiple concurrent connections
```

---

<div align="center">

## 🎉 Deployment Complete!

Your Medical Scribe AI is now deployed and ready for:
- ✅ Development and testing
- ✅ Small team use (Docker Compose)
- ✅ Enterprise production (Kubernetes)

### Next Steps

- 📚 [Configuration Guide](./LOCAL_LLM_GUIDE.md)
- 🔒 [Security Best Practices](./SECURITY.md)
- 📊 [Monitoring & Operations](./docs/OPERATIONS.md)

### Need Help?

- 🐛 [Report Issues](https://github.com/pimvic/Sumy/issues)
- 💬 [Community Discussions](https://github.com/pimvic/Sumy/discussions)

---

*Happy deploying!* 🚀

</div>

````