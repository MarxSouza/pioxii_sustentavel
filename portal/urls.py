from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pesquisa/form/', views.form, name='form'),
    url(r'^pesquisa/grafico/', views.grafico, name='grafico'),
    url(r'^sobre/', views.sobre, name='sobre'),
]