from django.db import models

# Create your models here.
class Product(models.Model):
    product_caption = models.CharField(max_length=20, verbose_name="Наименование продукта")
    price = models.PositiveIntegerField(verbose_name="Цена")
    quantity_in_stock = models.IntegerField(verbose_name="Количество на складе")

    def get_update_url(self):
        return reverse('edit_product', kwargs={'id': self.id})

    def __str__(self):
        return self.product_caption

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural ="Продукты"