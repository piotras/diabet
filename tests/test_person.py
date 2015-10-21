
import unittest

from diabet.manager import DiabetManager
from diabet.person_manager import PersonManager
from diabet.person import Person
from diabet.errors import ValueException, NoSuchPersonException

person_one_data = {
        'name': 'MalaMoo',
        'default_basal_rate': '0.7',
        'basal_rate': {
            '0': '0.9',
            '1': '1',
            '2': '1.2',
            '3': '1.2',
            '4': '1.3',
            '5': '1.4',
            '6': '1.4',
            '7': '1.3',
            '8': '1.4',
            '9': '1.3',
            '10': '1.2',
            '11': '1',
            '12': '0.8',
            '15': '0.6',
            '16': '0.6',
            '22': '0.8',
            '23': '0.8',
            },
        'default_icr': 8,
        'icr': {
            '8': 9,
            '9': 9,
            '10': 9,
            },
        }

class PersonTest(unittest.TestCase):

    def setUp(self):
        self.dm = DiabetManager()
        self.person_manager = self.dm.get_person_manager()
        self.person_one = Person(person_one_data)
   
    def test_get_name(self):
        self.assertEqual(self.person_one.get_name(), person_one_data['name'])

    def test_get_default_basal_rate(self):
        self.assertEqual(self.person_one.get_default_basal_rate(), person_one_data['default_basal_rate'])

    def test_set_default_basal_rate(self):
        self.person_one.set_default_basal_rate(0.9)
        self.assertEqual(self.person_one.get_default_basal_rate(), 0.9)

    def test_set_basal_rate_at(self):
        self.person_one.set_basal_rate_at(0.7, 3)
        self.person_one.set_basal_rate_at(0.6, 9)

    def test_get_basal_rate_at(self):
        self.person_one.set_basal_rate_at(0.7, 3)
        self.person_one.set_basal_rate_at(0.6, 9)

        self.assertEqual(self.person_one.get_basal_rate_at(3), 0.7)
        self.assertEqual(self.person_one.get_basal_rate_at(9), 0.6)

    def test_set_default_icr(self):
        self.person_one.set_default_icr(7)

    def test_set_default_icr_invalid(self):
        try:
            self.person_one.set_default_icr(-1)
        except ValueException:
            pass

    def test_get_default_icr(self):
        icr = 9
        self.person_one.set_default_icr(icr)
        self.assertEqual(self.person_one.get_default_icr(), icr)

    def test_set_icr_at(self):
        self.person_one.set_icr_at(7, 3)
        self.person_one.set_icr_at(6, 9)

    def test_get_icr_at(self):
        self.person_one.set_icr_at(7, 3)
        self.person_one.set_icr_at(6, 9)

        self.assertEqual(self.person_one.get_icr_at(3), 7)
        self.assertEqual(self.person_one.get_icr_at(9), 6)

    def test_set_default_isf(self):
        self.person_one.set_default_isf(30)

    def test_set_default_isf_invalid(self):
        try:
            self.person_one.set_default_isf(-1)
        except ValueException:
            pass

    def test_get_default_isf(self):
        isf = 9
        self.person_one.set_default_isf(isf)
        self.assertEqual(self.person_one.get_default_isf(), isf)

