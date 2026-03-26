# 🤝 Contributing to Medical Scribe AI - Sumy

Thank you for your interest in contributing to **Medical Scribe AI**! This guide will help you understand how to contribute code, documentation, and ideas to make this project better.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Types of Contributions](#types-of-contributions)
4. [Development Setup](#development-setup)
5. [Code Standards](#code-standards)
6. [Submitting Changes](#submitting-changes)
7. [Reporting Issues](#reporting-issues)
8. [Community](#community)

---

## 📜 Code of Conduct

### Our Commitment

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of:
- Age, body size, disability, ethnicity
- Gender identity and expression
- Experience level
- Nationality
- Personal appearance
- Race, religion, or sexual identity
- Background or education

### Expected Behavior

**We encourage:**
- ✅ Using welcoming and inclusive language
- ✅ Respecting different viewpoints and experiences
- ✅ Accepting constructive criticism gracefully
- ✅ Focusing on what's best for the community
- ✅ Showing empathy toward others

**We will not tolerate:**
- ❌ Harassment, bullying, or discrimination
- ❌ Offensive comments about personal characteristics
- ❌ Unwanted sexual attention or comments
- ❌ Threats or intimidation
- ❌ Any form of abuse or harassment

### Enforcement

Violations of the Code of Conduct will be addressed by project maintainers. Severe violations may result in removal from the project.

**Report concerns to**: [maintainers email - to be configured]

---

## 🚀 Getting Started

### Prerequisites

Before you start contributing, ensure you have:

```bash
# Git for version control
git --version

# Python 3.10+ for development
python3 --version

# pip for package management
pip --version

# Ollama for testing AI features (recommended)
ollama --version
```

### Fork & Clone

```bash
# 1. Fork on GitHub (click "Fork" button on repo page)

# 2. Clone your fork locally
git clone https://github.com/YOUR_USERNAME/Sumy.git
cd Sumy

# 3. Add upstream remote (for keeping in sync)
git remote add upstream https://github.com/pimvic/Sumy.git

# 4. Verify remotes
git remote -v
# Should show:
#   origin   https://github.com/YOUR_USERNAME/Sumy.git
#   upstream https://github.com/pimvic/Sumy.git
```

### Create Development Branch

```bash
# Update from upstream
git fetch upstream
git checkout main
git merge upstream/main

# Create feature branch
git checkout -b feature/your-feature-name

# Branch naming conventions:
# - feature/add-export-pdf      (new feature)
# - fix/auth-token-expire       (bug fix)
# - docs/update-readme           (documentation)
# - refactor/optimize-transcription (code improvement)
# - test/add-api-tests          (tests)
```

---

## 💼 Types of Contributions

### 🐛 Bug Fixes

**How to contribute:**
1. Find a bug in the code or documentation
2. Create branch: `git checkout -b fix/bug-name`
3. Fix the issue with tests
4. Submit pull request with "Fix:" prefix

**Example:**
```
Fix: JWT token expiration not refreshing properly

Description:
- Users were experiencing "Token Expired" errors
- The refresh endpoint was not properly implemented
- Now tokens refresh automatically

Tests:
- Added test_token_refresh_expired()
- Added test_concurrent_token_refresh()
```

### ✨ New Features

**How to contribute:**
1. Discuss feature in Issues first
2. Get approval from maintainers
3. Implement with tests
4. Submit pull request with "Feature:" prefix

### 📝 Documentation

**How to contribute:**
1. Identify unclear or missing documentation
2. Fork and create branch: `git checkout -b docs/topic`
3. Write clear, detailed documentation
4. Include code examples where relevant
5. Submit pull request

### 🧪 Tests

**How to contribute:**
1. Identify code without test coverage
2. Write comprehensive tests
3. Ensure tests pass: `pytest`
4. Check coverage: `pytest --cov`
5. Submit pull request with "Test:" prefix

### ⚡ Performance Improvements

**How to contribute:**
1. Identify performance bottleneck
2. Measure current performance: `pytest --benchmark`
3. Optimize the code
4. Verify improvement
5. Submit pull request with "Performance:" prefix

---

## 💻 Development Setup

### Environment Setup

```bash
# Navigate to project
cd Sumy

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Upgrade pip
pip install --upgrade pip

# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Pre-commit hooks (optional but recommended)
pip install pre-commit
pre-commit install

# Verify setup
python -m pytest tests/ -v
```

### Working with the Code

```bash
# Backend code
cd medical-scribe

# Start server in development mode (auto-reload)
python -m uvicorn backend.app.main:app --reload --port 8001

# In another terminal, run tests
pytest tests/ -v

# Check code coverage
pytest --cov=backend tests/

# Format code
black backend/ tests/

# Lint code
pylint backend/
mypy backend/ --ignore-missing-imports

# Run all checks
./run_checks.sh
```

---

## 📋 Code Standards

### Python Code Style

**Follow PEP 8 and use Black formatter:**

```bash
# Format code
pip install black
black backend/ hypocrate/

# Check style
pylint backend/
flake8 backend/

# Type checking
pip install mypy
mypy backend/ --ignore-missing-imports
```

**Organize imports:**
```python
# 1. Standard library imports
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# 2. Third-party imports
import numpy as np
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from pydantic import BaseModel, EmailStr

# 3. Local imports
from backend.app.config import settings
from backend.app.models import User, Recording
from backend.app.services import transcription, medical_notes
```

### Type Hints (Required)

All functions must have type hints:

```python
from typing import Dict, List, Optional, Tuple

def transcribe_audio(
    audio_path: str,
    language: str = "en",
    model_size: str = "base"
) -> Dict[str, any]:
    """
    Transcribe an audio file to text.
    
    Args:
        audio_path: Path to the audio file
        language: Language code (e.g., "en", "fr")
        model_size: Whisper model size
        
    Returns:
        Dictionary with transcription data
    """
    pass
```

### Docstrings (Required)

Use Google-style docstrings:

```python
def generate_soap_note(
    transcription: str,
    patient_id: int,
    specialty: str = "general"
) -> Dict[str, str]:
    """
    Generate a SOAP-formatted medical note.
    
    Args:
        transcription: Consultation text
        patient_id: Patient identifier
        specialty: Medical specialty
        
    Returns:
        Dictionary with SOAP components
    """
    pass
```

### Testing Standards

**Example unit test:**
```python
import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_user_registration():
    """Test user can register"""
    response = client.post(
        "/api/auth/register",
        json={
            "email": "test@example.com",
            "password": "TestPassword123!",
            "full_name": "Test User"
        }
    )
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"

def test_user_login():
    """Test user can login and get token"""
    response = client.post(
        "/api/auth/login",
        json={
            "email": "test@example.com",
            "password": "TestPassword123!"
        }
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
```

**Test coverage requirement:**
```bash
pytest --cov=backend --cov-report=html
# Must maintain 80%+ coverage
```

---

## 📤 Submitting Changes

### Commit Messages

**Format:**
```
<type>: <subject>

<body>

<footer>
```

**Types:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `style:` - Code style
- `refactor:` - Code refactoring
- `perf:` - Performance improvement
- `test:` - Test additions
- `chore:` - Build/dependency changes

**Example:**
```
feat: Add PDF export for medical notes

Add ability to export SOAP notes as formatted PDF files.
Users can customize font, logo, and header information.

Fixes: #123
```

### Creating Pull Requests

**Before submitting:**

```bash
# Update from upstream
git fetch upstream
git rebase upstream/main

# Run all tests
pytest tests/ -v

# Check code quality
black --check backend/
pylint backend/
mypy backend/

# Push to your fork
git push origin feature/your-feature-name
```

---

## 🐛 Reporting Issues

### Bug Reports

**Use this template:**

```markdown
## Description
Clear description of the bug

## Reproduction Steps
1. Step one
2. Step two
3. Step three

## Expected Behavior
What should happen

## Actual Behavior
What actually happened

## Environment
- OS: [macOS/Linux/Windows]
- Python version: [e.g., 3.10.5]
- Version: [e.g., 1.0.0]

## Error Messages
[Paste error messages/stack traces]
```

### Feature Requests

**Use this template:**

```markdown
## Description
Why is this feature needed?

## Use Case
How would this feature be used?

## Proposed Solution
How would you solve this?

## Alternatives
Other approaches you've considered
```

---

## 🗣️ Community

### Getting Help

- **Questions**: Use [GitHub Discussions](https://github.com/pimvic/Sumy/discussions)
- **Bugs**: Open [GitHub Issues](https://github.com/pimvic/Sumy/issues)
- **Security**: Email [security@sumy.ai]

### Contributing Outside Code

**We also welcome:**
- ✅ Writing blog posts or tutorials
- ✅ Creating video tutorials
- ✅ Sharing your use cases
- ✅ Helping other users
- ✅ Speaking at conferences

---

<div align="center">

## Thank You! 🙏

Your contributions make Medical Scribe AI better for everyone!

### Ready to Contribute?

1. **[Fork the repo](https://github.com/pimvic/Sumy/fork)**
2. **Start coding!**
3. **Submit a PR!**

---

*Questions? Open a [discussion](https://github.com/pimvic/Sumy/discussions)*  
*Found a bug? Report an [issue](https://github.com/pimvic/Sumy/issues)*

</div>
