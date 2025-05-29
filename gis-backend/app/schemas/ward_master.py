from pydantic import BaseModel
from typing import Optional

class WardMasterSchema(BaseModel):
    ward_id: Optional[int] = None
    ward_name: Optional[str] = "WARD NO. 1"

    class Config:
        from_attributes = True
