import factory
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    email = factory.LazyAttribute(
        lambda a: f"{a.name.replace(' ', '.').lower()}@gmail.com"
    )

    class Meta:
        model = User


class ExpertFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    email = factory.LazyAttribute(
        lambda a: f"{a.name.replace(' ', '.').lower()}@gmail.com"
    )
    is_expert = True

    class Meta:
        model = User
