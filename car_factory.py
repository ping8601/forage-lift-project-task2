from car import Car
from battery.battery import Battery
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SplindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire import carrigan_tire
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctiprimeTire

class CarFactory:
  @staticmethod
  def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_worn_level):
    engine = CapuletEngine(current_mileage, last_service_mileage)
    battery = SplindlerBattery(current_date, last_service_date)
    tire = CarriganTire(tire_worn_level)
    car = Car(engine, battery, tire)
    return car

  @staticmethod
  def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_worn_level):
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    battery = SplindlerBattery(current_date, last_service_date)
    tire = CarriganTire(tire_worn_level)
    car = Car(engine, battery, tire)
    return car
    
  @staticmethod
  def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage, tire_worn_level):
    engine = SternmanEngine(current_mileage, last_service_mileage)
    battery = SplindlerBattery(current_date, last_service_date)
    tire = OctiprimeTire(tire_worn_level)
    car = Car(engine, battery, tire)
    return car

  @staticmethod
  def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_worn_level):
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(current_date, last_service_date)
    tire = OctiprimeTire(tire_worn_level)
    car = Car(engine, battery, tire)
    return car

  @staticmethod
  def create_thevex(current_date, last_service_date, current_mileage, last_service_mileage, tire_worn_level):
    engine = CapuletEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(current_date, last_service_date)
    tire = OctiprimeTire(tire_worn_level)
    car = Car(engine, battery, tire)
    return car