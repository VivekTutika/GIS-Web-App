from sqlalchemy import Column, String, Text, Float, ForeignKey
from app.core.database import Base

class OtherDetails(Base):
    __tablename__ = "other_details"
    gis_id = Column(String(12), ForeignKey("survey_details.gis_id"), primary_key=True)
    source_of_water = Column(String(30), nullable=False)
    rain_water_harvesting_system = Column(String(3), default="NO", nullable=False)
    plantation = Column(String(3), default="NO", nullable=False)
    parking = Column(String(3), default="NO", nullable=False)
    pollution = Column(String(3), default="NO", nullable=False)
    pollution_measurement_taken = Column(Text)
    water_supply_within_200_meters = Column(String(3), default="NO", nullable=False)
    sewerage_line_within_100_meters = Column(String(3), default="NO", nullable=False)
    disposal_type = Column(String(10), nullable=False)
    total_plot_area = Column(Float, nullable=False)
    builtup_area_of_ground_floors = Column(Float, nullable=False)
    images_url = Column(Text, nullable=False)
    remarks = Column(Text)
