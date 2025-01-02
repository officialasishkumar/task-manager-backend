from fastapi import FastAPI
from .routers import auth, tasks
from .database import engine
from . import models
from fastapi.middleware.cors import CORSMiddleware
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="A simple Task Manager application with user authentication.",
    version="1.0.0",
)

origins = [
    "http://localhost:3001",  
    settings.FRONTEND_URL,  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router)
app.include_router(tasks.router)
