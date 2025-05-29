from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import mohalla_master as crud
from app.schemas.mohalla_master import MohallaMasterSchema
from app.api.deps import get_db

router = APIRouter(prefix="/mohallas", tags=["MohallaMaster"])

@router.get("/", response_model=list[MohallaMasterSchema])
async def read_mohallas(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_mohallas(db)

@router.get("/{mohalla_id}", response_model=MohallaMasterSchema)
async def read_mohalla(mohalla_id: int, db: AsyncSession = Depends(get_db)):
    mohalla = await crud.get_mohalla_by_id(db, mohalla_id)
    if not mohalla:
        raise HTTPException(status_code=404, detail="Mohalla not found")
    return mohalla

@router.post("/", response_model=MohallaMasterSchema)
async def create_mohalla(data: MohallaMasterSchema, db: AsyncSession = Depends(get_db)):
    return await crud.create_mohalla(db, data)

@router.delete("/{mohalla_id}", response_model=MohallaMasterSchema)
async def delete_mohalla(mohalla_id: int, db: AsyncSession = Depends(get_db)):
    mohalla = await crud.delete_mohalla(db, mohalla_id)
    if not mohalla:
        raise HTTPException(status_code=404, detail="Mohalla not found")
    return mohalla
