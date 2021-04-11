from django.contrib import admin
from .models import Type_customer, Сustomer

# Register your models here.

@admin.register(Сustomer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'middle_name', 'last_name', 'organization', 'phone')


admin.site.register(Type_customer)
# admin.site.register(Сustomer)