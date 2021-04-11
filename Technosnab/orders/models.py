from django.db import models
from cars.models import Cars
from workers.models import Worker
from customers.models import Сustomer
from services.models import Product


# Create your models here.
class Order(models.Model):
    car = models.ForeignKey(Cars, verbose_name="Автомобиль", on_delete=models.SET_NULL, null=True)
    worker = models.ForeignKey(Worker, verbose_name="Работник", on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Сustomer, verbose_name="Заказчик", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(verbose_name="Количество", null=True, blank=True)
    # time = models.IntegerField(verbose_name="Время", null=True, blank=True)
    final_price = models.IntegerField(verbose_name="Итоговая стоимость", null=True, blank=True)
    adress = models.CharField(max_length=20, verbose_name="Адрес")
    caption = models.CharField(max_length=300, verbose_name="Примечание", null=True, blank=True, default='-')
    STATUS = (
        ('С', 'Сompleted'),
        ('D', 'During'),
    )
    status = models.CharField(max_length=1, choices=STATUS, verbose_name="Статус", default='D', null=True)
    date = models.DateTimeField(null=True, verbose_name="Дата")
    # date = models.DateField(null=True, verbose_name="Дата")
    time = models.TimeField(verbose_name="Время", null=True, blank=True)
    def get_update_url(self):
        return reverse('edit_order', kwargs={'id': self.id})

    def __str__(self):
        return str(self.id) + " " + self.adress

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural ="Заказы"