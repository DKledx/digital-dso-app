class MockInitiativeRepository:
    def __init__(self):
        self.counter = 0

    def create_initiative(self, data):
        self.counter += 1
        return self.counter
