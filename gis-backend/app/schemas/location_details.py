from pydantic import BaseModel
from typing import Optional

class LocationDetailsSchema(BaseModel):
    gis_id: str
    property_latitude: float
    property_longitude: float
    assessment_year: int
    property_type: str
    building_name: Optional[str] = None
    road_type: str
    construction_year: int
    construction_type: str
    address_road_name: str
    locality: Optional[str] = None
    pin_code: int
    landmark: Optional[str] = None
    four_way_east: Optional[str] = None
    four_way_west: Optional[str] = None
    four_way_north: Optional[str] = None
    four_way_south: Optional[str] = None
    new_ward: str

    class Config:
        from_attributes = True
