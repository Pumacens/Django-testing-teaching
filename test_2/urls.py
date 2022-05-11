"""test_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
# Funcion que devuelve el HTML
from django.http import HttpResponse


def pagina_principal(request):

    return HttpResponse(
        '''
        <h1>Hola,estas en la pagina principal</h1>
        <h2>Subtitulo</h2>
        <a href="about/">Pagina de about</a>
        <a href="posts/">Pagina de posts</a>
        '''
    )


def pagina_about(request):
    return HttpResponse(
        '''
        <h1>Acerca de mi</h1>
        <h2>Proyecto por María Paz</h2>
        '''
    )



def que_te_pasa_loco(request):
    return HttpResponse(
        '''
        <h1>Jodete</h1>
        '''
    )


urlpatterns = [
    path('',  pagina_principal),
    path('about/',  pagina_about),
    path('posts/',  que_te_pasa_loco),
    path('admin/',      admin.site.urls)
]



