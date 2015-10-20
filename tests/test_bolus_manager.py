
import unittest

from diabet.manager import DiabetManager
from diabet.bolus_manager import BolusManager
from diabet.person import Person
from diabet.meal import Meal
from diabet.errors import ValueException, NoSuchPersonException

from .test_person import person_one_data

class BolusManagerTest(unittest.TestCase):

    def setUp(self):
        self.dm = DiabetManager()
        self.person_manager = self.dm.get_person_manager()
        self.person = Person(person_one_data)
        self.bolus_manager = self.dm.get_bolus_manager()
    
    def test_get_diabet_manager(self):
        self.assertEqual(self.dm, self.bolus_manager.get_diabet_manager())

    def test_calculate_bolus(self):
        expected_bolus = 6.9
        expected_extended_bolus = 1.1

        # chicken, pine, pepper, rise, oil
        meal = Meal('chicken', 55, 8, 27)
        bolus = self.dm.get_bolus_manager().calculate_bolus(self.person, meal)

        self.assertEqual(bolus.get_value(), expected_bolus)
        self.assertEqual(bolus.get_extended_value(), expected_extended_bolus)
