from pydantic import BaseModel
from typing import Optional

class OwnerDetailsSchema(BaseModel):
    gis_id: str
    owner_name: str
    father_husband_name: str
    mobile_number: Optional[str] = None
    aadhar_number: Optional[str] = None

    class Config:
        from_attributes = True
