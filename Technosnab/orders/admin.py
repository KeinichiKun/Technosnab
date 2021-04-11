from django.contrib import admin
from .models import Order
# Register your models here.

@admin.register(Order)
class OrderCAdmin(admin.ModelAdmin):
    autocomplete_fields = ('customer',)
# admin.site.register(Order)