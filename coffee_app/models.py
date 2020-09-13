from django.db import models

PRODUCT_TYPE_CHOICES = (
    ('COFFEE_MACHINE_LARGE', 'COFFEE MACHINE LARGE'),
    ('COFFEE_MACHINE_SMALL',  'COFFEE MACHINE SMALL'),
    ('ESPRESSO_MACHINE', 'ESPRESSO MACHINE'),
)

PRODUCT_TYPE_PODS_CHOICES = (
    ('COFFEE_POD_LARGE', 'COFFEE POD LARGE'),
    ('COFFEE_POD_SMALL',  'COFFEE POD SMALL'),
    ('ESPRESSO_POD', 'ESPRESSO POD'),
)

COFFEE_FLAVOR_CHOICES = (
    ('COFFEE_FLAVOR_VANILLA', 'COFFEE FLAVOR VANILLA'),
    ('COFFEE_FLAVOR_CARAMEL',  'COFFEE FLAVOR CARAMEL'),
    ('COFFEE_FLAVOR_PSL', 'COFFEE FLAVOR PSL'),
    ('COFFEE_FLAVOR_MOCHA',  'COFFEE FLAVOR MOCHA'),
    ('COFFEE_FLAVOR_HAZELNUT', 'COFFEE FLAVOR HAZELNUT'),
)

PACK_SIZE_CHOICES = (
    ('1_dozen(12)', '1 dozen (12)'),
    ('3_dozen(36)',  '3 dozen (36)'),
    ('5_dozen(60)', '5 dozen (60)'),
    ('7_dozen(84)', '7 dozen (84)'),
)


class CoffeeMachines(models.Model):
    product_type = models.CharField(max_length=70, choices=PRODUCT_TYPE_CHOICES, default='COFFEE_MACHINE_LARGE')
    water_line_compatible = models.BooleanField(default=False)
    code = models.CharField(max_length=6, unique=True)


class CoffeePods(models.Model):
    product_type = models.CharField(max_length=70, choices=PRODUCT_TYPE_PODS_CHOICES, default='COFFEE_POD_LARGE')
    coffee_flavor = models.CharField(max_length=70, choices=COFFEE_FLAVOR_CHOICES, default='COFFEE_FLAVOR_VANILLA')
    pack_size = models.CharField(max_length=70, choices=PACK_SIZE_CHOICES, default='1_dozen(12)')
    code = models.CharField(max_length=6, unique=True)

