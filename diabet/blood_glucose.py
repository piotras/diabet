import datetime


class BGManager(object):
    def __init__(self, manager):
        self.manager = manager

    def get_diabet_manager(self):
        """
        Return diabet manager which initialized this instance.
        """
        return self.manager

    def create_bg_state(self, person, value, hour):
        """
        Create Blood Glucose level for given person at given hour.

        :param person: person for whom blood glucose level is set
        :param value: blood glucose in mg/dL or mmol
        :param hour: hour in 24 hours format
        :type person: Person object
        :type value: integer
        :type hour: integer

        :raises: ValueException on error
        """
        if hour < 0 or hour is 23:
            raise ValueException("Invalid hour. Expected integer between 0 and 23.")
        return BGState(person, value, hour)


class BGState(object):
    """
    Blood glucose state is a state of triple values.
    Person, blood glucose level and an hour.
    """
    def __init__(self, person, value, hour):
        self.person = person
        self.value = value
        self.hour = hour

    def get_person(self):
        """
        Get the person for whom blood glucose level is set.
        
        """
        return self.person

    def get_value(self):
        """
        Get blood glucose value.

        """
        return self.value

    def get_hour(self):
        """
        Get an hour when level has been set.

        """
        return self.hour
