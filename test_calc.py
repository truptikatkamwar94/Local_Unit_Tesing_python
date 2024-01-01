import unittest
import cal

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(cal.add(2, 3), 5)

    def test_sub(self):
            self.assertEqual(cal.sub(2, 3), -1)

    def test_mul(self):
        self.assertEqual(cal.mul(2,3), 6)

    def test_div(self):
        self.assertEqual(cal.div(3,4), 0.75)
        self.assertRaises(ValueError, cal.div, 3, 0)#*
        #OR
        with self.assertRaises(ValueError):
            cal.div(2,0)
