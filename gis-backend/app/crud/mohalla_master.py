from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.mohalla_master import MohallaMaster
from app.schemas.mohalla_master import MohallaMasterSchema

async def get_all_mohallas(db: AsyncSession):
    result = await db.execute(select(MohallaMaster))
    return result.scalars().all()

async def get_mohalla_by_id(db: AsyncSession, mohalla_id: int):
    result = await db.execute(select(MohallaMaster).where(MohallaMaster.mohalla_id == mohalla_id))
    return result.scalar_one_or_none()

async def create_mohalla(db: AsyncSession, data: MohallaMasterSchema):
    new_mohalla = MohallaMaster(**data.model_dump())
    db.add(new_mohalla)
    await db.commit()
    await db.refresh(new_mohalla)
    return new_mohalla

async def delete_mohalla(db: AsyncSession, mohalla_id: int):
    mohalla = await get_mohalla_by_id(db, mohalla_id)
    if mohalla:
        await db.delete(mohalla)
        await db.commit()
    return mohalla
