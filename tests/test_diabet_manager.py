
import unittest

from manager import DiabetManager
from ..person_manager import PersonManager
from bolus_manager import BolusManager
from bolus_history_manager import BolusHistoryManager

class DiabetManagerTest(unittest.TestCase):

    def setUp(self):
        self.dm = DiabetManager()

    def test_diabet_manager(self):
        dm = DiabetManager()

    def test_get_person_manager(self):
        pm = self.dm.get_person_manager()
        self.assertTrue(isinstance(pm, PersonManager))

    def test_get_bolus_manager(self):
        pm = self.dm.get_bolus_manager()
        self.assertTrue(isinstance(pm, BolusManager))

    def test_get_bolus_history_manager(self):
        pm = self.dm.get_bolus_history_manager()
        self.assertTrue(isinstance(pm, BolusHistoryManager))


