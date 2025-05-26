from fastapi import APIRouter, Depends

from src.components.initiative_room.application.create_initiative_usecase import (
    CreateInitiativeUseCase,
)
from src.components.initiative_room.infrastructure.repo_mock import (
    MockInitiativeRepository,
)
from src.components.initiative_room.interface.schemas import (
    InitiativeCreateRequest,
    InitiativeCreateResponse,
)

router = APIRouter()


def get_use_case():
    repo = MockInitiativeRepository()
    return CreateInitiativeUseCase(repo)


@router.post("/initiative", response_model=InitiativeCreateResponse, status_code=201)
def create_initiative(
    request: InitiativeCreateRequest,
    use_case: CreateInitiativeUseCase = Depends(get_use_case),
):
    return use_case.execute(request)
