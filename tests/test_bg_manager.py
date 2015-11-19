
import unittest

from diabet.manager import DiabetManager
from diabet.blood_glucose import BGManager, BGLevel
from diabet.person import Person

from .test_person import person_one_data

class BGManagerTest(unittest.TestCase):

    def setUp(self):
        self.dm = DiabetManager()
        self.person = Person(person_one_data)
        self.bg_manager = self.dm.get_blood_glucose_manager()
    
    def test_get_diabet_manager(self):
        self.assertEqual(self.dm, self.bg_manager.get_diabet_manager())

    def test_create_bg_monitor(self):
        level = self.bg_manager.create_bg_level(self.person, 124)
        self.assertTrue(isinstance(level, BGLevel))
