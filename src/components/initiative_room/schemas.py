from datetime import datetime
from pydantic import BaseModel, Field, field_validator
import re

class InitiativeCreateRequest(BaseModel):
    name: str = Field(..., min_length=3)
    description: str
    quarter: str
    owner_unit: str
    expected_outcome: str

    @field_validator("quarter")
    @classmethod
    def validate_quarter_format(cls, v):
        if not re.match(r"Q[1-4]/20\d{2}", v):
            raise ValueError("quarter must be in format Qx/YYYY")
        return v

class InitiativeCreateResponse(BaseModel):
    id: int
    name: str
    description: str
    quarter: str
    owner_unit: str
    expected_outcome: str
    status: str = "draft"
    created_at: datetime