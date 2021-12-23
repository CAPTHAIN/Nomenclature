from django.core.management.base import BaseCommand
from main.models import *


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('args_id', nargs=2, type=int)

    def handle(self, *args, **options):
        categories = Category.objects.all()[:options['args_id'][0]]
        if categories:
            for cat in categories:
                print('-----')  # просто для красивого вывода :D
                print(cat)
                print('-----')
                product = Product.objects.filter(category=cat)[:options['args_id'][1]]
                for prod in product:
                    print(prod)  # сделал вывод поочередно, а не списком, опять же - для красоты и удобства)
        else:
            print("Введите хотя бы 1 категорию!")
