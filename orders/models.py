from django.db import models
from shop.models import Product


class OrderCountry(models.Model):
    name = models.CharField('Название страны', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна заказа'
        verbose_name_plural = 'Страна заказа'


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    country = models.ForeignKey(OrderCountry, on_delete=models.CASCADE, related_name='orders')
    email = models.EmailField(null=True, blank=True)
    note = models.TextField('Комментарий', null=True, blank=True)
    address = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
