from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.ward_master import WardMaster
from app.schemas.ward_master import WardMasterSchema

async def get_all_wards(db: AsyncSession):
    result = await db.execute(select(WardMaster))
    return result.scalars().all()

async def get_ward_by_id(db: AsyncSession, ward_id: int):
    result = await db.execute(select(WardMaster).where(WardMaster.ward_id == ward_id))
    return result.scalar_one_or_none()

async def create_ward(db: AsyncSession, data: WardMasterSchema):
    new_ward = WardMaster(**data.model_dump())
    db.add(new_ward)
    await db.commit()
    await db.refresh(new_ward)
    return new_ward

async def delete_ward(db: AsyncSession, ward_id: int):
    ward = await get_ward_by_id(db, ward_id)
    if ward:
        await db.delete(ward)
        await db.commit()
    return ward
