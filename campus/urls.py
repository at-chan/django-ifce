from django.contrib import admin
from django.urls import include, path
from apps.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace= 'core')),

]
