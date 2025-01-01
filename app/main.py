from fastapi import FastAPI
from .routers import auth, tasks
from .database import engine
from . import models
from fastapi.middleware.cors import CORSMiddleware
from .config import settings

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="A simple Task Manager application with user authentication.",
    version="1.0.0",
)

# CORS configuration
origins = [
    "http://localhost:3001",  # Frontend URL
    settings.FRONTEND_URL,  # Replace with actual frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Update with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router)
app.include_router(tasks.router)
