from pydantic import BaseModel
from typing import Optional

class OtherDetailsSchema(BaseModel):
    gis_id: str
    source_of_water: str
    rain_water_harvesting_system: str = "NO"
    plantation: str = "NO"
    parking: str = "NO"
    pollution: str = "NO"
    pollution_measurement_taken: Optional[str] = None
    water_supply_within_200_meters: str = "NO"
    sewerage_line_within_100_meters: str = "NO"
    disposal_type: str
    total_plot_area: float
    builtup_area_of_ground_floors: float
    images_url: str
    remarks: Optional[str] = None

    class Config:
        from_attributes = True
