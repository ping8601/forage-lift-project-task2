import unittest

import sys
sys.path.append('/Users/hungwanping/Documents/GitHub/forage-lyft-project')

from engine.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_no_need_service(self):
        current_mileage = 59999
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
