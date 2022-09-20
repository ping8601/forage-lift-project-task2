import unittest
from datetime import datetime

import sys
sys.path.append('/Users/hungwanping/Documents/GitHub/forage-lyft-project')

from battery.spindler_battery import SplindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(
            year = current_date.year - 4)
        battery = SplindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_no_need_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(
            year = current_date.year - 2)
        battery = SplindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
