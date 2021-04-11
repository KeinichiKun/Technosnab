from django.db import models
from workers.models import Worker

# Create your models here.

class Car_model(models.Model):
    caption_model = models.CharField(max_length=20, verbose_name="Наименование модели")

    def __str__(self):
        return self.caption_model

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural ="Модели"

class Car_specification(models.Model):
    caption_spec = models.CharField(max_length=20, verbose_name="Наименование спецификации")

    def __str__(self):
        return self.caption_spec

    class Meta:
        verbose_name = "Спецификация"
        verbose_name_plural ="Спецификации"

class Car_mark(models.Model):
    caption_mark = models.CharField(max_length=20, verbose_name="Наименование марки")

    def __str__(self):
        return self.caption_mark

    class Meta:
        verbose_name = "Марка"
        verbose_name_plural ="Марки"


class Cars(models.Model):
    state_number = models.CharField(max_length=7, verbose_name="Гос номер", unique=True)
    #expenses = models.PositiveIntegerField(verbose_name="Затраты", default=0)
    #income = models.PositiveIntegerField(verbose_name="Доход", default=0)
    #profit = models.IntegerField(verbose_name="Прибыль", default=0)
    Model_caption = models.CharField(max_length=30, verbose_name="Модель", null=True)
    Spec_caption = models.CharField(max_length=30, verbose_name="Спецификация", null=True)
    Mark_caption = models.CharField(max_length=30, verbose_name="Марка", null=True)
    carrying = models.PositiveIntegerField(verbose_name="Грузоподъемность", default=0)
    rent = models.PositiveIntegerField(verbose_name="Аренда", default=0)

    def get_update_url(self):
        return reverse('edit_car', kwargs={'id': self.id})

    def __str__(self):
        return self.state_number

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural ="Автомобили"
        ordering = ['state_number']


class Repairs_type(models.Model):
    description = models.CharField(max_length=400, verbose_name="Наименование типа ремонта")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Тип ремонта"
        verbose_name_plural = "Типы ремонтов"

class Repairs(models.Model):
    car = models.ForeignKey(Cars, verbose_name="Автомобиль", on_delete=models.SET_NULL, null=True)
    data_start = models.DateField(verbose_name="Время начала", null=True)
    data_end = models.DateField(verbose_name="Время окончания", null=True)
    description = models.CharField(max_length=400, verbose_name="Наименование запчасти")
    type = models.ForeignKey(Repairs_type, verbose_name="Тип ремонта", on_delete=models.SET_NULL, null=True)
    worker = models.ForeignKey(Worker, verbose_name="Исполнитель", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Ремонт"
        verbose_name_plural ="Ремонты"


class Expenses(models.Model):
    car = models.ForeignKey(Cars, verbose_name="Автомобиль", on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=400, verbose_name="Описание затраты", null=True, default='-')
    data = models.DateField(null=True)
    cost = models.IntegerField(verbose_name="Стоимость",null=True, default=0)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Затрата"
        verbose_name_plural ="Затраты"


class Profit(models.Model):
    car = models.ForeignKey(Cars, verbose_name="Автомобиль", on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=400, verbose_name="Описание прибыли")
    data = models.DateField(null=True)
    cost = models.IntegerField(verbose_name="Стоимость", default=0)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Прибыль"
        verbose_name_plural = "Прибыли"
