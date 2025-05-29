from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import owner_details as crud
from app.schemas.owner_details import OwnerDetailsSchema
from app.api.deps import get_db

router = APIRouter(prefix="/owners", tags=["OwnerDetails"])

@router.get("/{gis_id}", response_model=OwnerDetailsSchema)
async def read_owner(gis_id: str, db: AsyncSession = Depends(get_db)):
    owner = await crud.get_owner_details(db, gis_id)
    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    return owner

@router.post("/", response_model=OwnerDetailsSchema)
async def create_owner(data: OwnerDetailsSchema, db: AsyncSession = Depends(get_db)):
    return await crud.create_owner_details(db, data)

@router.put("/{gis_id}", response_model=OwnerDetailsSchema)
async def update_owner(gis_id: str, data: OwnerDetailsSchema, db: AsyncSession = Depends(get_db)):
    updated = await crud.update_owner_details(db, gis_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Owner not found")
    return updated

@router.delete("/{gis_id}", response_model=OwnerDetailsSchema)
async def delete_owner(gis_id: str, db: AsyncSession = Depends(get_db)):
    deleted = await crud.delete_owner_details(db, gis_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Owner not found")
    return deleted
