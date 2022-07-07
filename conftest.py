import pytest
from django.contrib.auth.models import User
from pytest_factoryboy import register
from shop_account.tests.factory import UserFactory
from shop_products.tests.factory import ProductsFactory, CategoriesFactory
from selenium import webdriver

# method 2 (better class based option)
register(UserFactory)  # can be accessed user_factory
register(ProductsFactory)  # can be accessed products_factory
register(CategoriesFactory)  # can be accessed categories_factory


@pytest.fixture
def create_product_factory_boy(db, products_factory):
    return products_factory.create()


@pytest.fixture
def create_category_factory_boy(db, categories_factory):
    return categories_factory.create()


@pytest.fixture
def factory_boy_superuser(user_factory):
    return user_factory.build()


# method 1
@pytest.fixture
def user_model_factory(db):
    def create_user(
            username: str,
            password: str = 'abc',
            is_staff: bool = False,
            is_superuser: bool = False,
            first_name: str = 'firstName',
            last_name: str = 'lastName',
            email: str = 'a@a.com',
    ):
        return User.objects.create_user(
            username=username,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

    return create_user


@pytest.fixture
def create_superuser(db, user_model_factory):
    return user_model_factory(username='aabc', password='123', email='a@a.com', is_superuser=True)


@pytest.fixture
def create_staff_user(db, user_model_factory):
    return user_model_factory(username='aabc', password='123', email='a@a.com', is_staff=True)


@pytest.fixture(scope='class')
def chrome_setup(request):
    browser = webdriver.Chrome()
    request.cls.browser = browser
    yield
    browser.quit()
