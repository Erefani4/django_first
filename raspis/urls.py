from django.urls import path
from . import views


urlpatterns = [
    path('', views.raspis_home, name='raspis_home'),
]