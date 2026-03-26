"""Main FastAPI application."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from .config import get_settings
from .database import init_db


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Add security headers to all responses."""
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "SAMEORIGIN"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        return response

settings = get_settings()

# Create FastAPI app
app = FastAPI(
    title="Medical Scribe API",
    description="AI-powered medical scribe application for automated clinical documentation",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Security headers middleware
app.add_middleware(SecurityHeadersMiddleware)

# CORS middleware configuration - restrictive for security
origins = settings.allowed_origins.split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
    expose_headers=["X-Total-Count"],
    max_age=600,  # Cache preflight 10 min
)


@app.on_event("startup")
async def startup_event():
    """Initialize database on startup."""
    init_db()


@app.get("/")
async def root():
    """Root endpoint - health check."""
    return {
        "message": "Welcome to Medical Scribe API",
        "version": "0.1.0",
        "status": "operational"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


# Import and include routers
from .routers import auth, recordings, transcribe
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(recordings.router, prefix="/api/recordings", tags=["Recordings"])
app.include_router(transcribe.router, prefix="/api/recordings", tags=["Transcription"])


if __name__ == "__main__":
    import uvicorn
    # Use 0.0.0.0 only for Docker/network deployment
    # For local testing, use 127.0.0.1 to prevent external exposure
    host = "127.0.0.1" if not settings.debug else "127.0.0.1"
    uvicorn.run(app, host=host, port=settings.api_port, reload=settings.debug)
