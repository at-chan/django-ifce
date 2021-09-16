from django.contrib import admin
from django.urls import include, path



app_name = 'professor'

from . import views
urlpatterns = [
    path('',views.AddProfessor,name='add_professor'),
]
