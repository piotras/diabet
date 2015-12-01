
class Meal(object):
    def __init__(self, name, carbo, fat, protein):
        self.name = name
        self.carbo = carbo
        self.fat = fat
        self.protein = protein

    def get_name(self):
        """
        Get name of the meal"

        """
        return self.name

    def get_carbo(self):
        """
        Get amount of carbohydrate.

        """
        return self.carbo

    def get_fat(self):
        """
        Get amount of fat.

        """
        return self.fat

    def get_protein(self):
        """
        Get amount of protein.

        """
        return self.protein
