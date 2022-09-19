from car import Car
from battery.battery import Battery
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SplindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory:
  @staticmethod
  def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = CapuletEngine(current_mileage, last_service_mileage)
    battery = SplindlerBattery(current_date, last_service_date)
    car = Car(engine, battery)
    return car

  @staticmethod
  def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    battery = SplindlerBattery(current_date, last_service_date)
    car = Car(engine, battery)
    return car
    
  @staticmethod
  def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = SternmanEngine(current_mileage, last_service_mileage)
    battery = SplindlerBattery(current_date, last_service_date)
    car = Car(engine, battery)
    return car

  @staticmethod
  def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(current_date, last_service_date)
    car = Car(engine, battery)
    return car

  @staticmethod
  def create_thevex(current_date, last_service_date, current_mileage, last_service_mileage):
    engine = CapuletEngine(current_mileage, last_service_mileage)
    battery = NubbinBattery(current_date, last_service_date)
    car = Car(engine, battery)
    return car