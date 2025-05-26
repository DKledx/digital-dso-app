from src.components.initiative_room.application.create_initiative_usecase import CreateInitiativeUseCase
from src.components.initiative_room.interface.schemas import InitiativeCreateRequest
from tests.components.initiative_room.mock_repo import MockInitiativeRepository

def test_create_initiative_success():
    repo = MockInitiativeRepository()
    use_case = CreateInitiativeUseCase(repo)
    request_data = InitiativeCreateRequest(
        name="Dự án DSO",
        description="Xây nền tảng quản lý chiến lược",
        quarter="Q3/2025",
        owner_unit="DSO",
        expected_outcome="Giao diện MVP"
    )
    response = use_case.execute(request_data)
    assert response.id == 1
    assert response.status == "draft"
    assert response.created_at is not None