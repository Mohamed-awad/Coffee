from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics


class CoffeeMachinesList(generics.ListAPIView):
    serializer_class = CoffeeMachinesSerializer

    def get_queryset(self):
        queryset = CoffeeMachines.objects.all()
        product_type = self.request.query_params.get('product_type', None)
        water_line_compatible = self.request.query_params.get('water_line_compatible', None)
        if product_type is not None:
            queryset = queryset.filter(product_type=product_type)
        if water_line_compatible is not None:
            if water_line_compatible == 'True':
                queryset = queryset.filter(water_line_compatible=True)
            elif water_line_compatible == 'False':
                queryset = queryset.filter(water_line_compatible=False)
            else:
                queryset = []
        return queryset


class CoffeePodsList(generics.ListAPIView):
    serializer_class = CoffeePodsSerializer

    def get_queryset(self):
        queryset = CoffeePods.objects.all()
        product_type = self.request.query_params.get('product_type', None)
        coffee_flavor = self.request.query_params.get('coffee_flavor', None)
        pack_size = self.request.query_params.get('pack_size', None)

        if product_type is not None:
            queryset = queryset.filter(product_type=product_type)
        if coffee_flavor is not None:
            queryset = queryset.filter(coffee_flavor=coffee_flavor)
        if pack_size is not None:
            queryset = queryset.filter(pack_size=pack_size)
        return queryset
