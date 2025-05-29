from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.owner_details import OwnerDetails
from app.schemas.owner_details import OwnerDetailsSchema

async def get_owner_details(db: AsyncSession, gis_id: str):
    result = await db.execute(select(OwnerDetails).where(OwnerDetails.gis_id == gis_id))
    return result.scalar_one_or_none()

async def create_owner_details(db: AsyncSession, data: OwnerDetailsSchema):
    owner = OwnerDetails(**data.model_dump())
    db.add(owner)
    await db.commit()
    await db.refresh(owner)
    return owner

async def update_owner_details(db: AsyncSession, gis_id: str, data: OwnerDetailsSchema):
    owner = await get_owner_details(db, gis_id)
    if not owner:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(owner, key, value)
    await db.commit()
    await db.refresh(owner)
    return owner

async def delete_owner_details(db: AsyncSession, gis_id: str):
    owner = await get_owner_details(db, gis_id)
    if owner:
        await db.delete(owner)
        await db.commit()
    return owner
