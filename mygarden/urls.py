from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('garden.urls','garden'),namespace='garden')),  # Inclui as URLs da app garden, sem namespace
]
