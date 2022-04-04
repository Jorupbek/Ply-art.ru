import requests
from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail
from orders.models import Order

logger = get_task_logger(__name__)
token = '5100919779:AAFPnAZxhiTF0LGjP6R54ZkCNZlUbkpvBHU'
chatid = '-726388449'

@shared_task()
def order_created(order_id):
    """Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    tg_msg = f'Новый заказ с сайта: \nИмя {order.first_name} \nНомер телефона{order.phone_number}'
    requests.get('https://api.telegram.org/bot{}/sendMessage'.format(token), params=dict(
        chat_id=chatid,
        text=tg_msg
    ))
    return mail_sent
