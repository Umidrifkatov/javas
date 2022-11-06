from django.contrib import admin
from main.models import Order

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Order, OrderAdmin)