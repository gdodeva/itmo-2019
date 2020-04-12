# -*- coding: utf-8 -*-

from datetime import date, datetime
from enum import Enum

from django.db import models


class Ingredient(models.Model):
    """A model that defines Ingredient object."""

    title = models.CharField(max_length=100)

    def __str__(self):
        """Returns string representation of Ingredient."""
        return self.title


class Pizza(models.Model):
    """A model that defines Pizza object."""

    title = models.CharField(max_length=100)
    price = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        """Returns string representation of Pizza."""
        return self.title

    def for_tests(self):
        """Returns string representation of Pizza."""
        return '{0} {1}'.format(self.title, self.price)


class OrderType(Enum):
    """A model that represents status of Order object."""

    def __str__(self):
        """Returns OrderType string representation."""
        return self.value


class Order(models.Model):
    """A model that defines Order object."""

    order_date = models.DateField(default=date.today)
    pizzas = models.ManyToManyField(Pizza)
    delivery_address = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=50)  # noqa: WPS432
    email_sent = models.BooleanField(default=False)
    status = models.CharField(
        max_length=50,  # noqa: WPS432
        choices=[
            ('ACCEPTED', 'ACCEPTED'),
            ('COOKING', 'COOKING'),
            ('DELIVERY', 'DELIVERY'),
            ('FINISHED', 'FINISHED'),
        ],
        default='ACCEPTED',
    )

    @property
    def delivery_time(self):
        """Calculates delivery time for Order."""
        working_hours = datetime.now().hour
        number_of_pizzas = self.pizzas.count()
        if working_hours >= 10 and working_hours < 22:  # noqa: WPS432, WPS333
            return number_of_pizzas * 10 + 40  # noqa: WPS432
        return number_of_pizzas * 10 + 60

    def __str__(self):
        """Returns string representation of Order."""
        return 'Oder date {0}. Status: {1}. Pizas: {2}'.format(self.order_date, self.status, self.pizzas.count())  # noqa: E501
