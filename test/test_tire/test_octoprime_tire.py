import unittest

import sys
sys.path.append('/Users/hungwanping/Documents/GitHub/forage-lyft-project')

from tire.octoprime_tire import OctiprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service(self):
        worn_level = [0.5, 0.8, 0.9, 0.8]
        tire = OctiprimeTire(worn_level)
        self.assertTrue(tire.needs_service())

    def test_no_need_service(self):
        worn_level = [0.5, 0.8, 0.8, 0.8]
        tire = OctiprimeTire(worn_level)
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()
