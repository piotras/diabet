
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

        # chicken, pineapple, pepper, rise, olive oil
        meal = Meal('chicken', 55, 8, 27)
        bg_state = self.dm.get_blood_glucose_manager().create_bg_state(self.person, 100, 14)
        bolus = self.dm.get_bolus_manager().calculate_bolus(bg_state, meal)

        self.assertEqual(bolus.get_value(), expected_bolus)
        self.assertEqual(bolus.get_extended_value(), expected_extended_bolus)

    def test_calculate_bolus_with_low_blood_glucose_level_mmol_set(self):
        # calculate bolus but suggest different one taking correction into account
        # set mmol measure for person
        raise NotImplementedError()

    def test_calculate_bolus_with_low_blood_glucose_level_mg_set(self):
        # calculate bolus but suggest different one taking correction into account
        # set mg/dL measure for person
        raise NotImplementedError()

    def test_calculate_bolus_with_high_blood_glucose_level_mmol_set(self):
        # calculate bolus but suggest different one taking correction into account
        # set mmol measure for person
        raise NotImplementedError()

    def test_calculate_bolus_with_high_blood_glucose_level_mg_set(self):
        # calculate bolus but suggest different one taking correction into account
        # set mg/dL measure for person
        raise NotImplementedError()

    def test_calculate_bolus_in_the_morning(self):
        expected_bolus = 4.8
        expected_extended_bolus = 0.8

        # bread, cheese, pineapple
        meal = Meal('breakfast', 43, 12, 9)
        bg_state = self.dm.get_blood_glucose_manager().create_bg_state(self.person, 100, 9)
        bolus = self.dm.get_bolus_manager().calculate_bolus(bg_state, meal)

        self.assertEqual(bolus.get_value(), expected_bolus)
        self.assertEqual(bolus.get_extended_value(), expected_extended_bolus)

    def test_calculate_bolus_in_the_evening(self):
        expected_bolus = 2.3
        expected_extended_bolus = 0.4

        # fruits, seeds
        meal = Meal('fruits', 18, 5, 3)
        bg_state = self.dm.get_blood_glucose_manager().create_bg_state(self.person, 100, 17)
        bolus = self.dm.get_bolus_manager().calculate_bolus(bg_state, meal)

        self.assertEqual(bolus.get_value(), expected_bolus)
        self.assertEqual(bolus.get_extended_value(), expected_extended_bolus)
