from django.contrib import admin
from .models import create, prod, orders

# Register your models here.
admin.site.register(create)
admin.site.register(prod)
admin.site.register(orders)
