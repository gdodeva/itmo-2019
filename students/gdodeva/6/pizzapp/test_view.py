# -*- coding: utf-8 -*-  # noqa: E902

from django.test import TestCase

from pizzapp.models import Ingredient, Pizza


class PostTest(TestCase):
    """Testing Views getting API."""

    def setUp(self):
        """Setting up database for testing purpose."""
        Ingredient.objects.create(
            title='Dough',
        )
        Ingredient.objects.create(
            title='Garlic',
        )
        royal = Pizza.objects.create(
            title='Royal common', price=200,  # noqa: WPS432
        )
        royal.ingredients.set([1])

        margaret = Pizza.objects.create(title='Margaret', price=90)  # noqa: WPS432, E501
        margaret.ingredients.set([2])

    def test_stats(self):
        """Checks accessibility of order API."""
        datas = {
            'pizzas': [1],
            'delivery_address': 'Vyazemsky 5',
            'customer_email': 'gabidodeva@gmail.com',
        }

        response = self.client.post(path='/api/order/', datas1=datas)
        assert response.status_code == 400  # noqa: WPS432

    def test_get(self):
        """Testing Views getting API Pizza."""
        response = self.client.get(path='/api/pizza/')
        assert response.status_code == 200  # noqa: WPS432

    def test_loading(self):
        """Tests for load."""
        response = self.client.get('/api/statistics/pizza')
        assert response.status_code == 200  # noqa: WPS432
        assert response.json() == {
            'all': 5,
            'pizzas': {'4': 2, '5': 3},
            'statuses': {'ACCEPTED': 3, 'COOKING': 2, 'DELIVERY': 0, 'FINISHED': 0},  # noqa: E501
        }
