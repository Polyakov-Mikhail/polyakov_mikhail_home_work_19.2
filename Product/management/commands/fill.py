import json
from django.core.management.base import BaseCommand
from Product.models import Product, Category


class Command(BaseCommand):
    """
    Кастомная команда, которая умеет заполнять данные в базу данных,
    при этом предварительно ее зачищать от старых данных из`fixtures/Product.json`.
    """

    @staticmethod
    def json_read_categories():
        """
        Чтение JSON файла с категориями товара
        """
        with open("fixtures/Product.json", encoding="utf-8") as file:
            data = json.load(file)
            return [item for item in data if item["model"] == "Product.category"]

    @staticmethod
    def json_read_products():
        """
        Чтение JSON файла с продуктами
        """
        with open("fixtures/Product.json", encoding="utf-8") as file:
            data = json.load(file)
            return [item for item in data if item["model"] == "Product.product"]

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        categories_for_create = []
        for item in Command.json_read_categories():
            category_data = item["fields"]
            categories_for_create.append(Category(id=item["pk"], **category_data))
        Category.objects.bulk_create(categories_for_create)

        products_for_create = []
        for item in Command.json_read_products():
            product_data = item["fields"]
            category = Category.objects.get(pk=product_data.pop("category"))
            products_for_create.append(
                Product(id=item["pk"], category=category, **product_data)
            )
        Product.objects.bulk_create(products_for_create)

        print("Success!")