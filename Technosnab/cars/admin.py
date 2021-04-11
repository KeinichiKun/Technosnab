from django.contrib import admin
from .models import Cars, Car_model, Car_specification, Car_mark, Profit, Expenses, Repairs, Repairs_type


admin.site.register(Cars)
admin.site.register(Car_model)
admin.site.register(Car_specification)
admin.site.register(Car_mark)
admin.site.register(Expenses)
admin.site.register(Profit)
admin.site.register(Repairs)
admin.site.register(Repairs_type)