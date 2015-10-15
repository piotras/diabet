
from errors import ValueException

class Person(object):
    def __init__(self, data=None):
        self.data = data

    def get_name(self):
        """
        Get the name of the person.

        :returns: name of the person
        :raises: ValueException on error
        """
        if self.data is None or 'name' not in self.data:
            raise ValueException("Missing name of the person")
        return self.data['name']
