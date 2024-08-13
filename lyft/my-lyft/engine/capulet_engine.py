from engine._engine import Engine

class CapuletEngine(Engine):
    def __init__(self, current_mileage, previous_mileage):
        self.current_mileage = current_mileage
        self.previous_mileage = previous_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
