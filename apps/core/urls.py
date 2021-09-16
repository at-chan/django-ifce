from django.urls import include, path



#a partir do Django 2 tem que criar o app_name
app_name = 'core'

#importa as views de core que está na mesma pasta
from . import views
urlpatterns = [
    path('', views.home, name='home'),
]