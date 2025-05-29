from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.survey_details import SurveyDetails
from app.schemas.survey_details import SurveyDetailsSchema

async def get_all_surveys(db: AsyncSession):
    result = await db.execute(select(SurveyDetails))
    return result.scalars().all()

async def get_survey_by_id(db: AsyncSession, gis_id: str):
    result = await db.execute(select(SurveyDetails).where(SurveyDetails.gis_id == gis_id))
    return result.scalar_one_or_none()

async def create_survey(db: AsyncSession, data: SurveyDetailsSchema):
    survey = SurveyDetails(**data.model_dump())
    db.add(survey)
    await db.commit()
    await db.refresh(survey)
    return survey

async def update_survey(db: AsyncSession, gis_id: str, data: SurveyDetailsSchema):
    survey = await get_survey_by_id(db, gis_id)
    if not survey:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(survey, key, value)
    await db.commit()
    await db.refresh(survey)
    return survey

async def delete_survey(db: AsyncSession, gis_id: str):
    survey = await get_survey_by_id(db, gis_id)
    if survey:
        await db.delete(survey)
        await db.commit()
    return survey
