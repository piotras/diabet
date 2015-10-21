
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
