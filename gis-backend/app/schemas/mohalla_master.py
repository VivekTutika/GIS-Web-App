from pydantic import BaseModel
from typing import Optional

class MohallaMasterSchema(BaseModel):
    mohalla_id: Optional[int] = None
    mohalla_name: Optional[str] = "Mohalla 1"

    class Config:
        from_attributes = True
