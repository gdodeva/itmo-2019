# -*- coding: utf-8 -*-

"""Django URL Routing for yumpi application."""

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from pizzapp.views import IngredientViewSet, PizzaViewSet, OrderViewSet, get_statistics, post_order  # noqa: I001, E501

router = routers.DefaultRouter()
router.register('pizza', PizzaViewSet)
router.register('ingredient', IngredientViewSet)
router.register('order_GET', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/order/', post_order),
    path('api/statistics/pizza', get_statistics),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
