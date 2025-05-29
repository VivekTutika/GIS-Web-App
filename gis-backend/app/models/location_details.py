from sqlalchemy import Column, String, Integer, Numeric, Text, ForeignKey
from app.core.database import Base

class LocationDetails(Base):
    __tablename__ = "location_details"
    gis_id = Column(String(12), ForeignKey("survey_details.gis_id"), primary_key=True)
    property_latitude = Column(Numeric(9, 6), nullable=False)
    property_longitude = Column(Numeric(9, 6), nullable=False)
    assessment_year = Column(Integer, nullable=False)
    property_type = Column(String(10), nullable=False)
    building_name = Column(Text)
    road_type = Column(String(40), nullable=False)
    construction_year = Column(Integer, nullable=False)
    construction_type = Column(String(20), nullable=False)
    address_road_name = Column(Text, nullable=False)
    locality = Column(Text)
    pin_code = Column(Integer, nullable=False)
    landmark = Column(Text)
    four_way_east = Column(Text)
    four_way_west = Column(Text)
    four_way_north = Column(Text)
    four_way_south = Column(Text)
    new_ward = Column(String(20), nullable=False)
