from django.contrib import admin
from django.urls import include, path
from apps.core import views
from apps.aluno import views


urlpatterns = [

    #adicionando a view do core
    path('admin/', admin.site.urls),
    path('aluno/', include('aluno.urls', namespace='aluno')),
    path('professor/', include('professor.urls', namespace='professor')),
    path('', include('core.urls', namespace='core')),
    

]
