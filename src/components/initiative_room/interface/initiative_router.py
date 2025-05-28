from fastapi import APIRouter, Depends, Request, HTTPException
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
    try:
        initiative_id = use_case.execute(payload)
        logger.info(f"Tạo SKCL thành công, id={initiative_id}", extra={"request_id": request.state.request_id})
        return InitiativeCreateResponse(id=initiative_id)
    except ValueError as e:
        logger.warning(f"Tạo SKCL thất bại: {e}", extra={"request_id": request.state.request_id})
        raise HTTPException(status_code=400, detail=str(e))