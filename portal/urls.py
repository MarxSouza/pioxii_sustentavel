from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^formulario/', views.formulario, name='formulario'),
    url(r'^grafico/', views.grafico, name='grafico'),
]
