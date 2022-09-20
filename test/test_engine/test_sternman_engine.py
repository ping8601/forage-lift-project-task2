import unittest

import sys
sys.path.append('/Users/hungwanping/Documents/GitHub/forage-lyft-project')

from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_need_service(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_no_need_service(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
