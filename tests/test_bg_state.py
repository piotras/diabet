import datetime
import unittest

from diabet.manager import DiabetManager
from diabet.blood_glucose import BGManager, BGState
from diabet.person import Person

from .test_person import person_one_data


class BGLevelTest(unittest.TestCase):

    def setUp(self):
        self.dm = DiabetManager()
        self.person = Person(person_one_data)
        self.bg_manager = self.dm.get_blood_glucose_manager()
        self.bg_value = 124
        self.bg_hour = 14
        self.bg_state = self.bg_manager.create_bg_state(self.person, self.bg_value, self.bg_hour)
    
    def test_get_person(self):
        person = self.bg_state.get_person()
        self.assertEqual(person, self.person)

    def test_get_value(self):
        value = self.bg_state.get_value()
        self.assertEqual(value, self.bg_value)

    def test_get_hour(self):
        hour = self.bg_state.get_hour()
        self.assertEqual(hour, self.bg_hour)
