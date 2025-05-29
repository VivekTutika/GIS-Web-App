from pydantic import BaseModel
from typing import Optional

class PropertyDetailsSchema(BaseModel):
    gis_id: str
    response_type: str
    old_house_number: str
    electricity_consumer_name: Optional[str] = None
    water_sewerage_connection_number: Optional[str] = None
    respondent_name: str
    respondent_status: str

    class Config:
        from_attributes = True
