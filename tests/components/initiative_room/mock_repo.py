class MockInitiativeRepository:
    def __init__(self):
        self._counter = 0

    def create_initiative(self, data):
        self._counter += 1
        return self._counter