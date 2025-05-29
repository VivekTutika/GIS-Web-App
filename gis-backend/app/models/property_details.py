from sqlalchemy import Column, String, ForeignKey
from app.core.database import Base

class PropertyDetails(Base):
    __tablename__ = "property_details"
    gis_id = Column(String(12), ForeignKey("survey_details.gis_id"), primary_key=True)
    response_type = Column(String(15), nullable=False)
    old_house_number = Column(String(15), nullable=False)
    electricity_consumer_name = Column(String(50))
    water_sewerage_connection_number = Column(String)
    respondent_name = Column(String(50), nullable=False)
    respondent_status = Column(String(10), nullable=False)
