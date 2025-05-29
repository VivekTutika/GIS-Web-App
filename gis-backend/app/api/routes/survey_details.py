from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import survey_details as crud
from app.schemas.survey_details import SurveyDetailsSchema
from app.api.deps import get_db

router = APIRouter(prefix="/surveys", tags=["SurveyDetails"])

@router.get("/", response_model=list[SurveyDetailsSchema])
async def read_surveys(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_surveys(db)

@router.get("/{gis_id}", response_model=SurveyDetailsSchema)
async def read_survey(gis_id: str, db: AsyncSession = Depends(get_db)):
    survey = await crud.get_survey_by_id(db, gis_id)
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    return survey

@router.post("/", response_model=SurveyDetailsSchema)
async def create_survey(data: SurveyDetailsSchema, db: AsyncSession = Depends(get_db)):
    return await crud.create_survey(db, data)

@router.put("/{gis_id}", response_model=SurveyDetailsSchema)
async def update_survey(gis_id: str, data: SurveyDetailsSchema, db: AsyncSession = Depends(get_db)):
    updated = await crud.update_survey(db, gis_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Survey not found")
    return updated

@router.delete("/{gis_id}", response_model=SurveyDetailsSchema)
async def delete_survey(gis_id: str, db: AsyncSession = Depends(get_db)):
    survey = await crud.delete_survey(db, gis_id)
    if not survey:
        raise HTTPException(status_code=404, detail="Survey not found")
    return survey
