import pytest

from shop_products.models import Products
from shop_products_category.models import ProductCategory
from faker import Faker
import factory

fake = Faker()


class CategoriesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductCategory

    name = fake.name()
    title = 'some-title'


class ProductsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Products

    title = fake.name()
    description = fake.text()
    price = 300_000
    # image =
    active = True

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for group in extracted:
                self.category.add(group)
