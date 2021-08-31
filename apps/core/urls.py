from django.urls import include, path

app_name = 'core'
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
