from django.contrib import admin
from .models import Position, Worker, Type_work, Tabel_time
from django.utils.safestring import mark_safe
# Register your models here.



@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'middle_name', 'first_name', 'last_name', )


    # def get_image(self, obj):
    #     return mark_safe(f'<img scr={obj.passport_img.url} width="50", height="60">')
    #
    #
    # get_image.short_description = "Изображение"

admin.site.register(Position)

admin.site.register(Type_work)
admin.site.register(Tabel_time)