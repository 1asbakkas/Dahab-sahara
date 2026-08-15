from django.contrib import admin
from .models import Atay, Customer, Order, OrderItem

admin.site.register(Atay)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)