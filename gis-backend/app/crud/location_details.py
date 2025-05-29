from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.location_details import LocationDetails
from app.schemas.location_details import LocationDetailsSchema

async def get_location_details(db: AsyncSession, gis_id: str):
    result = await db.execute(select(LocationDetails).where(LocationDetails.gis_id == gis_id))
    return result.scalar_one_or_none()

async def create_location_details(db: AsyncSession, data: LocationDetailsSchema):
    location = LocationDetails(**data.model_dump())
    db.add(location)
    await db.commit()
    await db.refresh(location)
    return location

async def update_location_details(db: AsyncSession, gis_id: str, data: LocationDetailsSchema):
    location = await get_location_details(db, gis_id)
    if not location:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(location, key, value)
    await db.commit()
    await db.refresh(location)
    return location

async def delete_location_details(db: AsyncSession, gis_id: str):
    location = await get_location_details(db, gis_id)
    if location:
        await db.delete(location)
        await db.commit()
    return location
