# -*- coding: utf-8 -*-

from django.core.mail import send_mail

from pizza.settings import EMAIL_HOST_USER


def send_mail_on_order(delivery_time: int, customer_email: str) -> None:
    """Sends email with order info to customer address."""
    send_mail(
        'Pizza mail',
        'Your order will be delivered to in {0} min.'.format(delivery_time),
        EMAIL_HOST_USER,
        [customer_email],
    )
