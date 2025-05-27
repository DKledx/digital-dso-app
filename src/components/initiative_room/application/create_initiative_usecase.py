from datetime import UTC, datetime
from src.components.initiative_room.schemas import (
    InitiativeCreateRequest, InitiativeCreateResponse
)

class CreateInitiativeUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, data: InitiativeCreateRequest) -> InitiativeCreateResponse:
        new_id = self.repository.create_initiative(data)
        return InitiativeCreateResponse(
            id=new_id,
            name=data.name,
            description=data.description,
            quarter=data.quarter,
            owner_unit=data.owner_unit,
            expected_outcome=data.expected_outcome
        )