from rest_framework import serializers
from .models import *


class CoffeeMachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeMachines
        fields = ['code']


class CoffeePodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeePods
        fields = ['code']
