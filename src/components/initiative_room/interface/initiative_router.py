from fastapi import APIRouter, Depends, Request
from src.shared.core.logger import get_logger
from src.components.initiative_room.application.create_initiative_usecase import CreateInitiativeUseCase
from src.components.initiative_room.infrastructure.repo_mock import MockInitiativeRepository
from src.components.initiative_room.schemas import InitiativeCreateRequest, InitiativeCreateResponse

router = APIRouter()
logger = get_logger(__name__)

def get_use_case():
    repo = MockInitiativeRepository()
    return CreateInitiativeUseCase(repo)

@router.post("/initiative", response_model=InitiativeCreateResponse, status_code=201)
def create_initiative(
    request: Request,
    payload: InitiativeCreateRequest,
    use_case: CreateInitiativeUseCase = Depends(get_use_case),
):
    logger.info("Đã nhận request tạo SKCL", extra={"request_id": request.state.request_id})
    return use_case.execute(payload)