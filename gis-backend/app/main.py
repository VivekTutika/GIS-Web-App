from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.database import engine, Base
from app.api.routes import (
    ward_master,
    mohalla_master,
    survey_details,
    property_details,
    owner_details,
    location_details,
    other_details
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # (Optional) Add any shutdown code here

app = FastAPI(
    title="GIS Survey Backend",
    description="API for handling survey-related operations securely",
    version="1.0.0",
    lifespan=lifespan
)

# CORS setup — allow frontend devs to test from localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(ward_master.router)
app.include_router(mohalla_master.router)
app.include_router(survey_details.router)
app.include_router(property_details.router)
app.include_router(owner_details.router)
app.include_router(location_details.router)
app.include_router(other_details.router)

@app.get("/", tags=["Health Check"])
async def root():
    return {"message": "GIS Survey Backend is online!"}
