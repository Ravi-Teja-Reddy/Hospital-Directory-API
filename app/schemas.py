

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class HospitalBase(BaseModel):
    name: str
    address: str
    phone: Optional[str] = None

class HospitalCreate(HospitalBase):
    pass

class HospitalUpdate(HospitalBase):
    pass

class HospitalResponse(HospitalBase):  
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
