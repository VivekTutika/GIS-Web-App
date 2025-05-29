from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import property_details as crud
from app.schemas.property_details import PropertyDetailsSchema
from app.api.deps import get_db

router = APIRouter(prefix="/properties", tags=["PropertyDetails"])

@router.get("/{gis_id}", response_model=PropertyDetailsSchema)
async def read_property(gis_id: str, db: AsyncSession = Depends(get_db)):
    property_data = await crud.get_property_details(db, gis_id)
    if not property_data:
        raise HTTPException(status_code=404, detail="Property not found")
    return property_data

@router.post("/", response_model=PropertyDetailsSchema)
async def create_property(data: PropertyDetailsSchema, db: AsyncSession = Depends(get_db)):
    return await crud.create_property_details(db, data)

@router.put("/{gis_id}", response_model=PropertyDetailsSchema)
async def update_property(gis_id: str, data: PropertyDetailsSchema, db: AsyncSession = Depends(get_db)):
    updated = await crud.update_property_details(db, gis_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Property not found")
    return updated

@router.delete("/{gis_id}", response_model=PropertyDetailsSchema)
async def delete_property(gis_id: str, db: AsyncSession = Depends(get_db)):
    deleted = await crud.delete_property_details(db, gis_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Property not found")
    return deleted
