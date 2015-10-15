
import json

from person import Person
from errors import NoSuchPersonException, DiabetException

class PersonManager(object):
    def __init__(self, manager):
        self._manager = manager
        self._data = None

    def get_diabet_manager(self):
        """
        Returns DiabetManager which created this instance.
        """
        return self._manager

    def get_person_by_name(self, name):
        """
        Get the person by given name.

        :param name: name of the person 

        :returns: Person object
        :raises: NoSuchPersonException if person with given name doesn't exist.
        """
        if self._data is None or name not in self._data:
            raise NoSuchPersonException
        
        return Person(self._data[name])

    def save_person(self, person):
        """
        Saves person in a storage.

        :param person: a person object to store
        :returns: None
        :raises: DiabetException on general error.
                 ValueException in case of invalid property of the person.
        """
        person_data = {}
        name = person.get_name()
        person_data['name'] = person.get_name()
        json_data = json.dumps(person_data)
        if self._data is None:
            self._data = {}
        self._data[name] = person_data
        with open('data.json', 'w') as f:
            json.dump(self._data, f)
