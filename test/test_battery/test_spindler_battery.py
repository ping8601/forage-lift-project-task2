import unittest
from datetime import datetime

from battery.spindler_battery import SplindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(
            year = current_date.year - 3)
        battery = SplindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_not_needs_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(
            year = current_date.year - 1)
        battery = SplindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
