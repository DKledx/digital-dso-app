from datetime import UTC, datetime

datetime.now(UTC)
from src.components.initiative_room.interface.schemas import (
    InitiativeCreateRequest,
    InitiativeCreateResponse,
)


class CreateInitiativeUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, data: InitiativeCreateRequest) -> InitiativeCreateResponse:
        new_id = self.repository.create_initiative(data)
        return InitiativeCreateResponse(
            id=new_id, status="draft", created_at=datetime.now(UTC)
        )
