from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import ward_master as crud
from app.schemas.ward_master import WardMasterSchema
from app.api.deps import get_db

router = APIRouter(prefix="/wards", tags=["WardMaster"])

@router.get("/", response_model=list[WardMasterSchema])
async def read_wards(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_wards(db)

@router.get("/{ward_id}", response_model=WardMasterSchema)
async def read_ward(ward_id: int, db: AsyncSession = Depends(get_db)):
    ward = await crud.get_ward_by_id(db, ward_id)
    if not ward:
        raise HTTPException(status_code=404, detail="Ward not found")
    return ward

@router.post("/", response_model=WardMasterSchema)
async def create_ward(data: WardMasterSchema, db: AsyncSession = Depends(get_db)):
    return await crud.create_ward(db, data)

@router.delete("/{ward_id}", response_model=WardMasterSchema)
async def delete_ward(ward_id: int, db: AsyncSession = Depends(get_db)):
    ward = await crud.delete_ward(db, ward_id)
    if not ward:
        raise HTTPException(status_code=404, detail="Ward not found")
    return ward
