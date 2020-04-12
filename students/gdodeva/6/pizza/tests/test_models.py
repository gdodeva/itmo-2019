from django.test import TestCase
from ..models import Ingredient, Pizza


class IngredientTest(TestCase):
    """ Test module for Puppy model."""

    def setUp(self):
        Ingredient.objects.create(
            title='Dough')
        Ingredient.objects.create(
            title='Garlic')

        royal = Pizza.objects.create(
            title='Royal common', price = 200)
        royal.ingredients.set([1])

        margaret = Pizza.objects.create(title='Margaret', price=90)
        margaret.ingredients.set([2])



    def test_ingredient_title(self):
        """ Test module for Ingredients model."""

        ingredient_dough = Ingredient.objects.get(title='Dough')
        ingredient_garlic = Ingredient.objects.get(title='Garlic')

        self.assertEqual(
            ingredient_dough.__str__(), "Dough")
        self.assertEqual(
            ingredient_garlic.__str__(), "Garlic")

    def test_pizza(self):
        """ Test module for Pizza model."""

        pizza_royal = Pizza.objects.get(title='Royal common')
        pizza_margaret = Pizza.objects.get(title='Margaret')

        self.assertEqual(
            pizza_royal.for_tests(), "Royal common 200")
        self.assertEqual(
            pizza_margaret.for_tests(), "Margaret 90")
