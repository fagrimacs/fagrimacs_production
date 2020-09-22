import factory

from accounts.factories import UserFactory
from .models import (TractorCategory, Tractor, Implement,
                     ImplementCategory, ImplementSubCategory)


class TractorCategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('random_choices', length=1, elements=(
        'Lawn Tractor', 'Garden Tractor', 'Subcompact Tractor',
        'Compact Utility Tractor', 'Earth moving Tractor',
        'Industrial Tractor Type'))

    class Meta:
        model = TractorCategory


class TractorFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    tractor_type = factory.SubFactory(TractorCategoryFactory)
    name = factory.Faker('bothify', text='John Deere ####?')
    file = factory.Faker('file_name', extension='jpg', category='image')
    engine_hp = factory.Faker('random_number', digits=3)
    drawbar_hp = factory.Faker('random_number', digits=3)
    pto_hp = factory.Faker('random_number', digits=3)
    hydraulic_capacity = factory.Faker('random_number', digits=3)
    fuel_consumption = factory.Faker('random_number', digits=3)
    price_hour = factory.Faker('random_number', digits=3)
    price_hectare = factory.Faker('random_number', digits=3)

    class Meta:
        model = Tractor


class ImplementCategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('random_choices', length=1, elements=(
        'Soil Cultivation', 'Planting', 'Fertilizing & Pest Control',
        'Drainage & Irrigation', 'Loading', 'Hay making', 'Other',
        'Harvesting & Post-Harvest'))

    class Meta:
        model = ImplementCategory


class ImplementSubCategoryFactory(factory.django.DjangoModelFactory):
    category = factory.Iterator(ImplementCategory.objects.all())
    name = factory.Faker('random_choices', length=1, elements=(
        'Soil Cultivation', 'Planting', 'Fertilizing & Pest Control',
        'Drainage & Irrigation', 'Loading', 'Hay making', 'Other',
        'Harvesting & Post-Harvest'))

    class Meta:
        model = ImplementSubCategory


class ImplementFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    name = factory.Faker('name')
    category = factory.SubFactory(ImplementCategoryFactory)
    subcategory = factory.SubFactory(ImplementSubCategoryFactory)
<<<<<<< HEAD
    file = factory.Faker('file_name', extension='jpg', category='image')
=======
>>>>>>> f9cc928... Add factories for models
    width = factory.Faker('numerify', text='%%')
    weight = factory.Faker('numerify', text='%%')
    pto = factory.Faker('random_number', digits=3)
    hydraulic_capacity = factory.Faker('random_number', digits=3)
    price_hour = factory.Faker('random_number', digits=3)
    price_hectare = factory.Faker('random_number', digits=3)

    class Meta:
        model = Implement
