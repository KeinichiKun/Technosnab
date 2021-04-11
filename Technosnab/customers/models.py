from django.db import models



# Create your models here.
class Type_customer(models.Model):
    type_cus_caption = models.CharField(max_length=30, verbose_name="Тип заказчика")

    def __str__(self):
        return self.type_cus_caption

    class Meta:
        verbose_name = "Тип заказчика"
        verbose_name_plural ="Типы заказчиков"

class Сustomer(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Имя", null=True, blank=True)
    middle_name = models.CharField(max_length=20, verbose_name="Фамилия", null=True, blank=True)
    last_name = models.CharField(max_length=20, verbose_name="Отчество", null=True, blank=True)
    organization = models.CharField(max_length=20, verbose_name="Организация", null=True, blank=True, default="-")
    adres = models.CharField(max_length=200, verbose_name="Адрес", null=True, blank=True, default="-")
    phone = models.CharField(max_length=12, verbose_name="Телефон", unique=True)
    T_customer = models.ForeignKey(Type_customer, verbose_name="Тип заказчика", on_delete=models.SET_NULL, null=True, default=2)
    inn = models.CharField(max_length=10, verbose_name="ИНН", null=True, blank=True, default="-")
    kpp = models.CharField(max_length=9, verbose_name="КПП", null=True, blank=True, default="-")
    bank = models.CharField(max_length=50, verbose_name="Банк", null=True, blank=True, default="-")
    rs = models.CharField(max_length=20, verbose_name="р/с", null=True, blank=True, default="-")
    ks = models.CharField(max_length=20, verbose_name="Корр. счет", null=True, blank=True, default="-")
    bik = models.CharField(max_length=9, verbose_name="БИК", null=True, blank=True, default="-")
    email = models.CharField(max_length=40, verbose_name="E-mail", null=True, blank=True, default="-")


    def get_update_url(self):
        return reverse('edit_customer', kwargs={'id': self.id})

    def __str__(self):

            if self.first_name == None:
                return "+" + self.phone
            else:
                return self.first_name + " " + self.middle_name + " " + self.last_name + " " + self.organization


    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural ="Заказчики"