
class BGManager(object):
    def __init__(self, manager):
        self.manager = manager

    def get_diabet_manager(self):
        """
        Return diabet manager which initialized this instance.
        """
        return self.manager

    def create_bg_monitor(self, person, bg_level):
        """
        Create Blood Glucose monitor for given person.

        """
        return BGMonitor(person, bg_level)


class BGMonitor(object):
    def __init__(self, person, bg_level):
        self.person = person
        self.bg_level = bg_level
        # FIXME, set proper hour
        self.hour = None

    def get_person(self):
        """
        Get the person for whom monitor is set.
        
        """
        return self.person

    def get_bg_level(self):
        """
        Get blood glucose level.

        """
        return self.bg_level

    def get_hour(self):
        """
        Get an hour when monitor has been initialized.

        """
        return self.hour


