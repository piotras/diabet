
import unittest

from diabet.meal import Meal

class MealTest(unittest.TestCase):

    def setUp(self):
        self.name = 'Chicken with vegetables'
        self.carbo = 55
        self.fat = 8
        self.protein = 27
        self.meal = Meal(self.name, self.carbo, self.fat, self.protein)

    def test_get_name(self):
        self.assertEqual(self.meal.get_name(), self.name)

    def test_get_carbo(self):
        self.assertEqual(self.meal.get_carbo(), self.carbo)

    def test_get_fat(self):
        self.assertEqual(self.meal.get_fat(), self.fat)

    def test_get_protein(self):
        self.assertEqual(self.meal.get_protein(), self.protein)

