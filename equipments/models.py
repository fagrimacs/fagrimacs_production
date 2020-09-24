from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField

from django.contrib.auth import get_user_model

User = get_user_model()


class TractorCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tractor_category',
                              blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Tractor Categories'

    def __str__(self):
        return self.name


DRIVE_TYPE = (
    (None, 'Please Select'),
    ('two wheel drive', 'Two wheel Drive'),
    ('four wheel drive', 'Four wheel Drive'),
)
TRANSMISSION_MODE = (
    (None, 'Please Select'),
    ('gear', 'Gear'),
    ('manual', 'Manual'),
    ('hydrostatic', 'Hydrostatic'),
    ('turbochanged', 'Turbocharged'),
)
HITCHING_TYPE = (
    (None, 'Please Select'),
    ('two point hitches', 'Two-point hitches'),
    ('three point hitches', 'Three-point hitches'),
)
ATTACHMENT_MODE = (
    (None, 'Please select'),
    ('frontend loader', 'frontend loader'),
    ('backhoe', 'Backhoe'),
    ('both', 'Both'),
)
FARM_SERVICES = (
    ('soil cultivations', 'Soil cultivations'),
    ('planting', 'Planting'),
    ('haversting/post-haversting', 'Haversting/Post-Haversting'),
    ('fertilizing & pest-control', 'Fertilizing & Pest-control'),
    ('drainage & irrigation', 'Drainage & Irrigation'),
    ('loading', 'Loading'),
    ('hay making', 'Hay making'),
    ('miscellaneous', 'Miscellaneous'),
)


class Tractor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tractor_type = models.ForeignKey(
        TractorCategory, verbose_name='What type of Tractor?',
        on_delete=models.SET('others'))
    drive_type = models.CharField(
        max_length=100, verbose_name='What Drive Type', choices=DRIVE_TYPE)
    name = models.CharField(
        max_length=200, verbose_name='Name/Models of Tractor',
        help_text='eg. John Deere 6190R')
    mode_of_transmission = models.CharField(
        max_length=100, verbose_name='Mode of Transmission',
        choices=TRANSMISSION_MODE)
    engine_hp = models.PositiveIntegerField(
        verbose_name='Engine Horse Power (eg. 75hp)')
    drawbar_hp = models.PositiveIntegerField(
        verbose_name='Drawbar Horse Power (eg. 65hp)')
    pto_hp = models.PositiveIntegerField(
        verbose_name='PTO Horse Power (eg. 85hp)')
    hydraulic_capacity = models.CharField(
        max_length=100, help_text='Use a SI units of gpm or psi',
        verbose_name=('Hydaulic capacity (gallon per minutes(gpm)'
                      ' or psi-pound per square inchies)'))
    type_of_hitching = models.CharField(
        max_length=100, verbose_name='What is Hitching type?',
        choices=HITCHING_TYPE)
    cab = models.BooleanField(verbose_name='Does have a cab?', default=False)
    rollover_protection = models.BooleanField(
        verbose_name='Does have the rollover protection?', default=False)
    fuel_consumption = models.PositiveIntegerField(
        verbose_name='Fuel consumption (gallon per hour on operation)')
    attachment_mode = models.CharField(
        max_length=100, verbose_name='What mode of attachment?',
        choices=ATTACHMENT_MODE)
    operator = models.BooleanField(default=False,
                                   verbose_name='Do you have an operator(s)?')
    file = models.FileField(
        upload_to='tractors_photos/',
        verbose_name='Upload the Tractor pictures',
        help_text=('Upload quality picture of real tractor you have,'
                   ' only 5 picture.'))
    other_informations = models.TextField(
        blank=True, verbose_name='Describe your Tractor')
    price_hour = models.PositiveIntegerField(
        verbose_name='Specify the price per Hour in TShs.')
    price_hectare = models.PositiveIntegerField(
        verbose_name='Specify the price per Hectare')
    farm_services = MultiSelectField(
        choices=FARM_SERVICES,
        verbose_name='What are farming service(s) do you offer?')
    agree_terms = models.BooleanField(
        default=False, verbose_name='Do your Accept our Terms and Conditions?')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('equipments:tractor-detail', kwargs={'pk': self.id})


class ImplementCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='implements_category',
                              blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Implement Categories'

    def __str__(self):
        return self.name


class ImplementSubCategory(models.Model):
    category = models.ForeignKey(ImplementCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Implement Subcategories'

    def __str__(self):
        return self.name


OPERATION_MODE = (
    (None, 'Please Select'),
    ('tractor drive', 'Tractor drive'),
    ('self-propelled', 'Self-propelled'),
)


class Implement(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=100, verbose_name='Name/Models of Implement')
    category = models.ForeignKey(
        ImplementCategory, on_delete=models.SET('others'),
        verbose_name='What category of your Implement')
    subcategory = models.ForeignKey(
        ImplementSubCategory, on_delete=models.SET('others'),
        verbose_name='What is subcategory of your Implement')
    width = models.PositiveIntegerField(
        verbose_name='Width of the Implement', help_text='SI UNITS in metre',)
    weight = models.PositiveIntegerField(
        verbose_name='Weight of the Implement', help_text='SI UNITS in KG')
    operation_mode = models.CharField(
        max_length=100, choices=OPERATION_MODE,
        verbose_name='What is mode of operation?')
    pto = models.PositiveIntegerField(
        verbose_name='What is Horse Power required for Operation?')
    hydraulic_capacity = models.CharField(
        max_length=100,
        verbose_name='What is Hydaulic capacity required to lift?')
    operator = models.BooleanField(verbose_name='Do you have an operator(s)?')
    file = models.FileField(
        upload_to='implements_photos/',
        verbose_name='Upload the Implement pictures',
        help_text=("Upload quality picture of real implement you have,"
                   " only 5 pictures."))
    other_informations = models.TextField(
        blank=True, verbose_name='Describe your Implement')
    price_hour = models.PositiveIntegerField(
        verbose_name='Specify the price per Hour')
    price_hectare = models.PositiveIntegerField(
        verbose_name='Specify the price per Hectare')
    agree_terms = models.BooleanField(
        default=False, verbose_name='Do your Accept our Terms and Conditions?')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('equipments:implement-detail', kwargs={'pk': self.id})
