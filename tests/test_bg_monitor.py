
import unittest

from diabet.manager import DiabetManager
from diabet.blood_glucose import BGManager, BGMonitor
from diabet.person import Person

from .test_person import person_one_data

class BGMonitorTest(unittest.TestCase):

    def setUp(self):
        self.dm = DiabetManager()
        self.person = Person(person_one_data)
        self.bg_manager = self.dm.get_blood_glucose_manager()
        self.bg_level = 124
        self.bg_monitor = self.bg_manager.create_bg_monitor(self.person, self.bg_level)
    
    def test_get_person(self):
        person = self.bg_monitor.get_person()
        self.assertEqual(person, self.person)

    def test_get_bg_level(self):
        level = self.bg_monitor.get_bg_level()
        self.assertEqual(level, self.bg_level)

    def test_get_hour(self):
        raise NotImplementedError()
