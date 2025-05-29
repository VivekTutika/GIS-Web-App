from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import other_details as crud
from app.schemas.other_details import OtherDetailsSchema
from app.api.deps import get_db

router = APIRouter(prefix="/others", tags=["OtherDetails"])

@router.get("/{gis_id}", response_model=OtherDetailsSchema)
async def read_other(gis_id: str, db: AsyncSession = Depends(get_db)):
    other = await crud.get_other_details(db, gis_id)
    if not other:
        raise HTTPException(status_code=404, detail="Other details not found")
    return other

@router.post("/", response_model=OtherDetailsSchema)
async def create_other(data: OtherDetailsSchema, db: AsyncSession = Depends(get_db)):
    return await crud.create_other_details(db, data)

@router.put("/{gis_id}", response_model=OtherDetailsSchema)
async def update_other(gis_id: str, data: OtherDetailsSchema, db: AsyncSession = Depends(get_db)):
    updated = await crud.update_other_details(db, gis_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Other details not found")
    return updated

@router.delete("/{gis_id}", response_model=OtherDetailsSchema)
async def delete_other(gis_id: str, db: AsyncSession = Depends(get_db)):
    deleted = await crud.delete_other_details(db, gis_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Other details not found")
    return deleted
