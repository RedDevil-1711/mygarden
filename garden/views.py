from django.shortcuts import render
from .models import Plant

def plant_list(request):
     plants=Plant.objects.select_related('group').all()
     return render(request,'garden/plant_list.html',{'plants':plants})
