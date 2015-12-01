import datetime


class BGManager(object):
    def __init__(self, manager):
        self.manager = manager

    def get_diabet_manager(self):
        """
        Return diabet manager which initialized this instance.
        """
        return self.manager

    def create_bg_level(self, person, value):
        """
        Create Blood Glucose level for given person.

        """
        return BGLevel(person, value)


class BGLevel(object):
    def __init__(self, person, value):
        self.person = person
        self.value = value
        # TODO: ensure time conversion is also valid for daylight saving offset
        self.hour = datetime.datetime.now(self.person.get_timezone()).hour

    def get_person(self):
        """
        Get the person for whom level is set.
        
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
