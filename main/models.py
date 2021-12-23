from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='Имя')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='Имя')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    status = models.CharField(max_length=12, choices=[('in_stock', 'In stock'), ('out_of_stock', 'Out of stock')],
                              verbose_name='Статус')
    remains = models.IntegerField(verbose_name='Остаток')

    def __str__(self):
        return self.name


@receiver(post_save, sender=Product)
def clear_cache(sender, instance, **kwargs):
    cache.clear()
