
import unittest

from diabet.manager import DiabetManager
from diabet.person_manager import PersonManager
from diabet.person import Person
from diabet.errors import ValueException, NoSuchPersonException

class PersonManagerTest(unittest.TestCase):

    def setUp(self):
        self.dm = DiabetManager()
        self.person_manager = self.dm.get_person_manager()
        self.person_one_data = {
                'name': 'Alice',
                'default_basal_rate': '0.7',
                }
    
    def test_get_diabet_manager(self):
        self.assertEqual(self.dm, self.person_manager.get_diabet_manager())

    def test_get_person_by_name(self):
        person = Person(self.person_one_data)
        self.person_manager.save_person(person)

        name = 'Alice'
        new_person = self.person_manager.get_person_by_name(name)
        self.assertEqual(new_person.get_name(), name) 
    
    def test_get_person_by_name_invalid_name(self):
        try:
            new_person = self.person_manager.get_person_by_name('NoSuchName')
            self.assertIsNone(new_person)
        except NoSuchPersonException:
            pass

    def test_save_person_create(self):
        person = Person(self.person_one_data)
        self.person_manager.save_person(person)

    def test_save_person_create_invalid_name(self):
        person = Person()
        try:
            self.person_manager.save_person(person)
        except ValueException:
            pass

    def test_save_person_update(self):
        person = Person(self.person_one_data)
        self.person_manager.save_person(person)

        # set new default_basal_rate
        new_rate = 0.9
        person.set_default_basal_rate(new_rate)
        self.person_manager.save_person(person)

        new_person = self.person_manager.get_person_by_name('Alice')
        self.assertEqual(new_person.get_default_basal_rate(), new_rate)
