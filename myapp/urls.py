# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Маршрут для корневого URL
    path('data/', views.data_view, name='data'),
    path('test/', views.test_view, name='test'),
]
