from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime



# Create your models here.
class Position(models.Model):
    position_caption = models.CharField(max_length=20, verbose_name="Наименование должности")

    def __str__(self):
        return self.position_caption

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural ="Должности"

class Type_work(models.Model):
    work = models.CharField(max_length=20, verbose_name="Наименование занятости")
    salary = models.CharField(max_length=20, verbose_name="Зарплата")

    def __str__(self):
        return self.work

    class Meta:
        verbose_name = "Тип работы"
        verbose_name_plural ="Типы работы"

class Worker(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    middle_name = models.CharField(max_length=20, verbose_name="Фамилия")
    last_name = models.CharField(max_length=20, verbose_name="Отчество")
    phone = models.CharField(max_length=12, verbose_name="Телефон", unique=True)
    passport_seria = models.CharField(max_length=4, verbose_name="Серия Паспорта")
    passport_number = models.CharField(max_length=6, verbose_name="Номер Паспорта")
    passport_issued = models.CharField(max_length=100, verbose_name="Паспорт выдан")
    passport_date = models.DateField(verbose_name="Дата выдачи", null=True)
    adress = models.CharField(max_length=100, verbose_name="Адрес")
    P_position = models.ForeignKey(Position, verbose_name="Должность", null=True, on_delete=models.SET_NULL)
    T_work = models.ForeignKey(Type_work, verbose_name="Тип работы", null=True, on_delete=models.SET_NULL)
    time = models.IntegerField(verbose_name="Время работы", null=True)
    passport_img = models.ImageField(null=True, blank=True, upload_to="pasport_img/", verbose_name="Скан паспорта")

    def get_update_url(self):
        return reverse('edit_worker', kwargs={'id': self.id})

    def __str__(self):
        return self.middle_name + " " + self.first_name + " " + self.last_name

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural ="Работники"


class Tabel_time(models.Model):

    worker = models.ForeignKey(Worker, verbose_name="Сотрудник", null=True, on_delete=models.SET_NULL)
    day1 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day2 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day3 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day4 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day5 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day6 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day7 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day8 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day9 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day10 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day11 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day12 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day13 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day14 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day15 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day16 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day17 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day18 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day19 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day20 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day21 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day22 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day23 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day24 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day25 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day26 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day27 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day28 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day29 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day30 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    day31 = models.IntegerField(verbose_name="Количество часов", null=True, default=0)
    data = models.DateField(null=True)

