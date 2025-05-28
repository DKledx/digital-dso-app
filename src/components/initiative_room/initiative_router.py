from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.shared.core.db import get_db_session
from src.components.initiative_room.infrastructure.repo_sqlalchemy import InitiativeRepository
from src.components.initiative_room.application.use_cases import CreateInitiativeUseCase
from src.components.initiative_room.application.requests import InitiativeCreateRequest

router = APIRouter()

@router.post("/initiative")
def create_initiative(request: InitiativeCreateRequest, db: Session = Depends(get_db_session)):
    repo = InitiativeRepository(db)
    use_case = CreateInitiativeUseCase(repo)
    return use_case.execute(request)
