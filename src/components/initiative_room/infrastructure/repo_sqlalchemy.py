from src.components.initiative_room.infrastructure.models import InitiativeModel
from sqlalchemy.orm import Session

class InitiativeRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    def create_initiative(self, data):
        record = InitiativeModel(**data.dict(), status="draft")
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)
        return record.id
