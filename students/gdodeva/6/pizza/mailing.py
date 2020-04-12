# -*- coding: utf-8 -*-

from django.core.mail import send_mail

from pizzapp.settings import EMAIL_HOST_USER


def send_mail_on_order(delivery_time: int, customer_email: str, customer_address: str) -> None:  # noqa: E501
    """Sends email with order info to customer address."""
    send_mail(
        'Pizza mail',
        'Your order will be delivered to {0} in {1} min.'.format(customer_address, delivery_time),  # noqa: E501
        EMAIL_HOST_USER,
        [customer_email],
    )
