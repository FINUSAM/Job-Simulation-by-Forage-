from battery._battery import Battery

class Nubbin(Battery):
    def __init__(self, current_date, last_service_data):
        self.current_date = current_date
        self.last_service_data = last_service_data
        
    def needs_service(self):
        return self.current_date - self.last_service_data > 4
