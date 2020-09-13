from . import views
from django.urls import path

app_name = 'coffee_app'

urlpatterns = [
    path('machines/', views.CoffeeMachinesList.as_view(), name='machines_list'),
    path('pods/', views.CoffeePodsList.as_view(), name='pods_list'),
]
