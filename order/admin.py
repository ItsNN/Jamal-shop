from django.contrib import admin
from .models import Order, OrderItem
# Register  models here.
admin.site.register(Order)
admin.site.register(OrderItem)