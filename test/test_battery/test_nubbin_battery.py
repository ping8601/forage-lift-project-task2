import unittest
from datetime import datetime

import sys
sys.path.append('/Users/hungwanping/Documents/GitHub/forage-lyft-project')

from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(
            year = current_date.year - 5)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_no_needs_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(
            year = current_date.year - 3)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()