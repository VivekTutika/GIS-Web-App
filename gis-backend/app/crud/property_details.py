from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.property_details import PropertyDetails
from app.schemas.property_details import PropertyDetailsSchema

async def get_property_details(db: AsyncSession, gis_id: str):
    result = await db.execute(select(PropertyDetails).where(PropertyDetails.gis_id == gis_id))
    return result.scalar_one_or_none()

async def create_property_details(db: AsyncSession, data: PropertyDetailsSchema):
    details = PropertyDetails(**data.model_dump())
    db.add(details)
    await db.commit()
    await db.refresh(details)
    return details

async def update_property_details(db: AsyncSession, gis_id: str, data: PropertyDetailsSchema):
    details = await get_property_details(db, gis_id)
    if not details:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(details, key, value)
    await db.commit()
    await db.refresh(details)
    return details

async def delete_property_details(db: AsyncSession, gis_id: str):
    details = await get_property_details(db, gis_id)
    if details:
        await db.delete(details)
        await db.commit()
    return details
