from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'garden'  # Definindo app_name para usar namespace (opcional, mas recomendado)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),

    path('', views.plant_list, name='plant_list'),
    path('plant/<int:plant_id>/', views.plant_detail, name='plant_detail'),
    path('add_plant/', views.add_plant, name='add_plant'),
    path('add_content/', views.add_content, name='add_content'),
    path('add_group/', views.add_group, name='add_group'),
    path('add_plant_to_user/<int:plant_id>/', views.add_plant_to_user, name='add_plant_to_user'),
    path('remove_plant_from_user/<int:plant_id>/', views.remove_plant_from_user, name='remove_plant_from_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
