from sqlalchemy import Column, String, TIMESTAMP, DECIMAL
from sqlalchemy.sql import func
from app.core.database import Base

class SurveyDetails(Base):
    __tablename__ = "survey_details"
    gis_id = Column(String(12), primary_key=True, nullable=False)
    ulb = Column(String(50), nullable=False, default="ULB NAME")
    zone = Column(String(20), nullable=False, default="ZONE 1")
    ward = Column(String(20), nullable=False)
    mohalla = Column(String(50), nullable=False)
    survey_unique_code = Column(String(50), nullable=False)
    entry_date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    map_id = Column(DECIMAL(6, 10), nullable=False)
    sub_gis_id = Column(String(12))
    parcel_id = Column(DECIMAL(6, 10))
