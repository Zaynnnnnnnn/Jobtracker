from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import jobs, users, auth
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="JobTracker API",
    description="A full-stack job application tracking system",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router, prefix="/api/auth", tags=["authentication"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(jobs.router, prefix="/api/jobs", tags=["jobs"])

@app.get("/")
def read_root():
    return {"message": "Welcome to JobTracker API!"}

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "service": "JobTracker API"}
