from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import datetime

class SurveyDetailsSchema(BaseModel):
    gis_id: str
    ulb: str = "ULB NAME"
    zone: str = "ZONE 1"
    ward: str
    mohalla: str
    survey_unique_code: str
    entry_date: Optional[datetime] = None
    map_id: Decimal
    sub_gis_id: Optional[str] = None
    parcel_id: Optional[Decimal] = None

    class Config:
        from_attributes = True
