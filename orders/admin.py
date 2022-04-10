from django.contrib import admin
from orders.models import Order, OrderItem, OrderCountry


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone_number', 'email', 'address', )
    inlines = [OrderItemInline]


admin.site.register(OrderCountry)