from sqlalchemy import Column, String, ForeignKey
from app.core.database import Base

class OwnerDetails(Base):
    __tablename__ = "owner_details"
    gis_id = Column(String(12), ForeignKey("survey_details.gis_id"), primary_key=True)
    owner_name = Column(String(50), nullable=False)
    father_husband_name = Column(String(50), nullable=False)
    mobile_number = Column(String(10))
    aadhar_number = Column(String(12))
