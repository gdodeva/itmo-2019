from django.test import TestCase
from ..models import Ingredient, Pizza


class PostTest(TestCase):
    """Testing Views getting API."""

    def setUp(self):
        """Setting up database for testing purpose."""
        Ingredient.objects.create(
            title='Dough')
        Ingredient.objects.create(
            title='Garlic')
        royal = Pizza.objects.create(
            title='Royal common', price=200)
        royal.ingredients.set([1])

        margaret = Pizza.objects.create(title='Margaret', price=90)
        margaret.ingredients.set([2])

    def test_stats(self):
        """Checks accessibility of order API."""
        data = {
            "pizzas": [0],
            "delivery_address": "murinskaya 61",
            "customer_email": "artvolk981@gmail.com"
        }

        response = self.client.post(path='/api/order/', data=data)
        assert response.status_code == 400

class TestGetPizzas(TestCase):
    """Testing Views getting API Pizza class."""

    def setUp(self):
        """Setting up database for testing purpose."""
        Ingredient.objects.create(
            title='Dough')
        Ingredient.objects.create(
            title='Garlic')
        royal = Pizza.objects.create(
            title='Royal common', price=200)
        royal.ingredients.set([1])

        margaret = Pizza.objects.create(title='Margaret', price=90)
        margaret.ingredients.set([2])

    def test_get(self):
        """Testing Views getting API Pizza."""
        response = self.client.get(path='/api/pizza/')
        assert response.status_code == 200


class TestStatistics(TestCase):
    """Setting up database for testing purpose Statistics."""

    def setUp(self):
        """Setting up database for testing purpose."""
        Ingredient.objects.create(
            title='Dough')
        Ingredient.objects.create(
            title='Garlic')
        royal = Pizza.objects.create(
            title='Royal common', price=200)
        royal.ingredients.set([1])

        margaret = Pizza.objects.create(title='Margaret', price=90)
        margaret.ingredients.set([2])
        data = {
            "pizzas": [1],
            "delivery_address": "murinskaya 61",
            "customer_email": "artvolk981@gmail.com"
        }

        self.client.post(path='/api/order/', data=data)

    def test_loading(self):
        """Tests for load."""
        response = self.client.get('/api/statistics/pizza')
        assert response.status_code == 200
        assert response.json() == {
            'all': 1,
            'pizzas': {'1': 1},
            'statuses': {'ACCEPTED': 1, 'COOKING': 0, 'DELIVERY': 0, 'FINISHED': 0},
        }

