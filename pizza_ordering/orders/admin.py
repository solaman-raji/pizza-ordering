from django.contrib import admin

from .models import Order, OrderDeliveryStatus

admin.site.register(Order)
admin.site.register(OrderDeliveryStatus)
