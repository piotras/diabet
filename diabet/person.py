
from errors import ValueException

class Person(object):
    def __init__(self, data={}):
        self.data = data

    def _validate_key_in_data(self, key, error):
        if key not in self.data:
            raise ValueException(error)

    def get_name(self):
        """
        Get the name of the person.

        :returns: name of the person
        :raises: ValueException on error
        """
        self._validate_key_in_data('name', 'Missing name of the person')
        return self.data['name']

    def set_default_basal_rate(self, rate):
        """
        Sets default basal rate.

        Basal Rate: The rate at which an insulin pump infuses small, “background” doses of short-acting insulin.
        http://www.diabetesselfmanagement.com/diabetes-resources/definitions/basal-rate/

        Basal rate 0 is allowed because person might not have insulin pump.
        With traditional injections, basal rate can not be set.

        :raises: ValueException in case of invalid rate.
        """
        if rate < 0:
            raise ValueException('Invalid, negative value of basal rate')
        self.data['default_basal_rate'] = rate

    def get_default_basal_rate(self):
        """
        Get default basal rate.

        :raises: ValueException in case of invalid value.
        """
        self._validate_key_in_data('default_basal_rate', 'Missing  default_basal_rate')
        return self.data['default_basal_rate']
