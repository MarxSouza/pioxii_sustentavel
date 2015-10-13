from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pesquisa/formulario/', views.formulario, name='formulario'),
    url(r'^pesquisa/grafico/', views.grafico, name='grafico'),
    url(r'^sobre/', views.sobre, name='sobre'),
    url(r'^download/app/', views.baixarapp, name='baixarapp'),
]