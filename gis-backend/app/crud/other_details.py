from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.other_details import OtherDetails
from app.schemas.other_details import OtherDetailsSchema

async def get_other_details(db: AsyncSession, gis_id: str):
    result = await db.execute(select(OtherDetails).where(OtherDetails.gis_id == gis_id))
    return result.scalar_one_or_none()

async def create_other_details(db: AsyncSession, data: OtherDetailsSchema):
    other = OtherDetails(**data.model_dump())
    db.add(other)
    await db.commit()
    await db.refresh(other)
    return other

async def update_other_details(db: AsyncSession, gis_id: str, data: OtherDetailsSchema):
    other = await get_other_details(db, gis_id)
    if not other:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(other, key, value)
    await db.commit()
    await db.refresh(other)
    return other

async def delete_other_details(db: AsyncSession, gis_id: str):
    other = await get_other_details(db, gis_id)
    if other:
        await db.delete(other)
        await db.commit()
    return other
