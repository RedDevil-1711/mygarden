from django.urls import path
from . import views

urlpatterns=[
    path('plants/',views.plant_list,name='plant_list'),
]
