# -*- coding: utf-8 -*-

from django.test import TestCase

from pizzapp.models import Ingredient, Pizza  # noqa: WPS300


class IngredientTest(TestCase):
    """Test module for Puppy model."""

    def setUp(self):
        """Setting up."""
        Ingredient.objects.create(
            title='Dough',
        )
        Ingredient.objects.create(
            title='Garlic',
        )

        royal = Pizza.objects.create(
            title='Royal common', price=200,  # noqa: WPS432
        )  # noqa: WPS432
        royal.ingredients.set([1])

        margaret = Pizza.objects.create(
            title='Margaret', price=90,  # noqa: WPS432
        )
        margaret.ingredients.set([2])

    def test_ingredient_title(self):
        """Test module for Ingredients model."""
        ingredient_dough = Ingredient.objects.get(title='Dough')
        ingredient_garlic = Ingredient.objects.get(title='Garlic')
        self.assertEqual(  # noqa: T003
            ingredient_dough.__str__(), 'Dough',  # noqa: WPS609
        )
        self.assertEqual(  # noqa: T003
            ingredient_garlic.__str__(), 'Garlic',  # noqa: WPS609
        )

    def test_pizza(self):
        """Test module for Pizza model."""
        pizza_royal = Pizza.objects.get(title='Royal common')
        pizza_margaret = Pizza.objects.get(title='Margaret')
        self.assertEqual(  # noqa: T003
            pizza_royal.for_tests(), 'Royal common 200',
        )
        self.assertEqual(  # noqa: T003
            pizza_margaret.for_tests(), 'Margaret 90',
        )
