
import unittest

from diabet.bolus import Bolus

class BolusTest(unittest.TestCase):

    def setUp(self):
        self.value = 5
        self.extended = 1
        self.bolus = Bolus(self.value, self.extended)

    def test_get_value(self):
        self.assertEqual(self.bolus.get_value(), self.value)

    def test_get_extended_value(self):
        self.assertEqual(self.bolus.get_extended_value(), self.extended)
