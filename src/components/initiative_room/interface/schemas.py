from datetime import datetime

from pydantic import BaseModel, Field


class InitiativeCreateRequest(BaseModel):
    name: str = Field(..., min_length=3)
    description: str = Field(..., max_length=1000)
    quarter: str  # ví dụ: Q3/2025
    owner_unit: str
    expected_outcome: str


class InitiativeCreateResponse(BaseModel):
    id: int
    status: str = "draft"
    created_at: datetime
