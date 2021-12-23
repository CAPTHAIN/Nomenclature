from django.core.management.base import BaseCommand
from main.models import *
from random import randint


class Command(BaseCommand):

    def handle(self, *args, **options):
        products = Product.objects.all()

        for product in products:
            status = ['in_stock', 'out_of_stock']

            product.remains = randint(1, 999)
            product.price = randint(1, 999)
            product.status = status[randint(0, 1)]
            product.save()
