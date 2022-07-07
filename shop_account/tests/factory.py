import factory
from faker import Faker
from django.contrib.auth.models import User

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username: str = fake.name()
    password: str = '123'
    is_staff: bool = False
    is_superuser: bool = False
    first_name: str = 'firstName'
    last_name: str = 'lastName'
    email: str = 'a@a.com'
