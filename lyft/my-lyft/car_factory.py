from car import Car
from battery.nubbin import Nubbin
from battery.splinder import Splinder
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory():
    
    def create_calliope(self, current_mileage, previous_mileage, current_date, last_service_data):
        engine = CapuletEngine(current_mileage, previous_mileage)
        battery = Splinder(current_date, last_service_data)
        car = Car(engine, battery)
        return car
    
    def create_glissade(self, current_mileage, previous_mileage, current_date, last_service_data):
        engine = WilloughbyEngine(current_mileage, previous_mileage)
        battery = Splinder(current_date, last_service_data)
        car = Car(engine, battery)
        return car
    
    def create_palindrome(self, current_mileage, previous_mileage, current_date, last_service_data):
        engine = SternmanEngine(current_mileage, previous_mileage)
        battery = Splinder(current_date, last_service_data)
        car = Car(engine, battery)
        return car
    
    def create_rorschach(self, current_mileage, previous_mileage, current_date, last_service_data):
        engine = WilloughbyEngine(current_mileage, previous_mileage)
        battery = Nubbin(current_date, last_service_data)
        car = Car(engine, battery)
        return car
    
    def create_thovex(self, current_mileage, previous_mileage, current_date, last_service_data):
        engine = CapuletEngine(current_mileage, previous_mileage)
        battery = Nubbin(current_date, last_service_data)
        car = Car(engine, battery)
        return car
