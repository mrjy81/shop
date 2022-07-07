import pytest
from shop_products.models import Products


def test_product(create_product_factory_boy):
    assert True


@pytest.mark.parametrize(
    "title , name , validity",
    [
        ('hello', 'world', True),
        ('hello', '', False),
    ],
    scope='module'
)
def test_category(
        db, categories_factory, title, name, validity
):
    test = categories_factory(
        title=title,
        name=name,
    )


@pytest.mark.parametrize(
    "title , description , price , active ,validity",
    [
        ('hello', 'hello world', 300_000, True, True),
        ('hello', 'hello world', 300_000, False, False),
    ],
    scope='module'

)
def test_products(
        db, products_factory, title, description, price, active, validity
):
    test = products_factory.create(
        title=title,
        description=description,
        price=price,
        active=active,
    )
    # print(Products.objects.all().count())
