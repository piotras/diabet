
from person_manager import PersonManager
from bolus_manager import BolusManager
from bolus_history_manager import BolusHistoryManager

class DiabetManager(object):
    person_manager = None
    bolus_manager = None
    bolus_history_manager = None

    def get_person_manager(self):
        """
        Returns PersonManager.

        PersonManager is created only once and always the same instance is returned.
        """
        if self.person_manager is None:
            self.person_manager = PersonManager(self)
        return self.person_manager

    def get_bolus_manager(self):
        """
        Returns BolusManager.

        BolusManager is created only once and always the same instance is returned.
        """
        if self.bolus_manager is None:
            self.bolus_manager = BolusManager(self)
        return self.bolus_manager

    def get_bolus_history_manager(self):
        """
        Returns BolusHistoryManager.

        BolusHistoryManager is created only once and always the same instance is returned.
        """
        if self.bolus_history_manager is None:
            self.bolus_history_manager = BolusHistoryManager(self)
        return self.bolus_history_manager
