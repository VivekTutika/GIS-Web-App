from sqlalchemy import Column, Integer, String
from app.core.database import Base

class WardMaster(Base):
    __tablename__ = "ward_master"
    ward_id = Column(Integer, primary_key=True, autoincrement=True)
    ward_name = Column(String(12), default="WARD NO. 1")
