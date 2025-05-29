from sqlalchemy import Column, Integer, String
from app.core.database import Base

class MohallaMaster(Base):
    __tablename__ = "mohalla_master"
    mohalla_id = Column(Integer, primary_key=True, autoincrement=True)
    mohalla_name = Column(String(12), default="Mohalla 1", nullable=False)
