from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import location_details as crud
from app.schemas.location_details import LocationDetailsSchema
from app.api.deps import get_db

router = APIRouter(prefix="/locations", tags=["LocationDetails"])

@router.get("/{gis_id}", response_model=LocationDetailsSchema)
async def read_location(gis_id: str, db: AsyncSession = Depends(get_db)):
    location = await crud.get_location_details(db, gis_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

@router.post("/", response_model=LocationDetailsSchema)
async def create_location(data: LocationDetailsSchema, db: AsyncSession = Depends(get_db)):
    return await crud.create_location_details(db, data)

@router.put("/{gis_id}", response_model=LocationDetailsSchema)
async def update_location(gis_id: str, data: LocationDetailsSchema, db: AsyncSession = Depends(get_db)):
    updated = await crud.update_location_details(db, gis_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Location not found")
    return updated

@router.delete("/{gis_id}", response_model=LocationDetailsSchema)
async def delete_location(gis_id: str, db: AsyncSession = Depends(get_db)):
    deleted = await crud.delete_location_details(db, gis_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Location not found")
    return deleted
