












# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import data, user
from backend.utils.logger import init_logging

app = FastAPI(
    title="AuroraVault API",
    description="Backend API for zk-based private data exchange.",
    version="0.1.0",
)

# Allow CORS for frontends
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_logging()

# Routers
app.include_router(data.router, prefix="/data", tags=["Data Exchange"])
app.include_router(user.router, prefix="/user", tags=["User"])

@app.get("/")
def root():
    return {"AuroraVault": "Zero-Knowledge Privacy Network is running."}
