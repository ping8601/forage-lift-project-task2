import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SplindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestBattery(unittest.TestCase):
    def test_NubbinBattery_should_be_serviced(self):
        self.current_date = datetime.today().date()
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 5)
        self.assertTrue(NubbinBattery.needs_service(self))

    def test_NubbinBattery_should_not_be_serviced(self):
        self.current_date = datetime.today().date()
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 3)
        self.assertFalse(NubbinBattery.needs_service(self))

    def test_SpindlerBattery_should_be_serviced(self):
        self.current_date = datetime.today().date()
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 3)
        self.assertTrue(SplindlerBattery.needs_service(self))

    def test_SpindlerBattery_should_not_be_serviced(self):
        self.current_date = datetime.today().date()
        self.last_service_date = self.current_date.replace(
            year=self.current_date.year - 1)
        self.assertFalse(SplindlerBattery.needs_service(self))


class TestEngine(unittest.TestCase):
    def test_CapuletEngine_should_be_serviced(self):
        self.current_mileage = 30001
        self.last_service_mileage = 0
        self.assertTrue(CapuletEngine.needs_service(self))

    def test_CapuletEngine_should_not_be_serviced(self):
        self.current_mileage = 29999
        self.last_service_mileage = 0
        self.assertFalse(CapuletEngine.needs_service(self))

    def test_SternmanEngine_should_be_serviced(self):
        self.warning_light_is_on = True
        self.assertTrue(SternmanEngine.needs_service(self))

    def test_SternmanEngine_should_not_be_serviced(self):
        self.warning_light_is_on = False
        self.assertFalse(SternmanEngine.needs_service(self))
    
    def test_WilloughbyEngine_should_be_serviced(self):
        self.current_mileage = 60001
        self.last_service_mileage = 0
        self.assertTrue(WilloughbyEngine.needs_service(self))

    def test_WilloughbyEngine_should_not_be_serviced(self):
        self.current_mileage = 59999
        self.last_service_mileage = 0
        self.assertFalse(WilloughbyEngine.needs_service(self))




if __name__ == '__main__':
    unittest.main()
