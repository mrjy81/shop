import pytest
from django.contrib.auth.models import User


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
    return user_model_factory(username='abc', password='123', email='a@a.com', is_superuser=True)


@pytest.fixture
def create_staff_user(db, user_model_factory):
    return user_model_factory(username='abc', password='123', email='a@a.com', is_staff=True)
