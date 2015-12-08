
from .bolus import Bolus

class BolusManager(object):
    def __init__(self, manager):
        self.manager = manager

    def get_diabet_manager(self):
        """
        Return diabet manager which initialized this instance.
        """
        return self.manager

    def calculate_bolus(self, bg_status, meal):
        """
        Calculate bolus for given blood glucose level and meal.

        """
        person = bg_status.get_person()
        icr = float(person.get_icr_at(bg_status.get_hour()))
        # TODO, blood glucose level is required to compute valid bolus for current blood glucose level
        # calculate simple bolus
        # divide amount of carbohydrates (grammes) by person's icr
        simple_bolus_value = float(meal.get_carbo()) / icr
        # calculate extended bolus
        # multiply fat by 9
        fat = int(meal.get_fat()) * 9
        # multiply protein by 4
        protein = int(meal.get_protein()) * 4
        # sum fat and protein, divide by 10 and then by person's icr
        # then divide by 2 to get amount of insulin required for given fat and protein
        ext_bolus_value = ((float(fat + protein)) / 10 / icr) / 2
        return Bolus(round(simple_bolus_value, 1), round(ext_bolus_value, 1))
