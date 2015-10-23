from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^formulario.py', views.formulario, name='formulario'),
    url(r'^grafico.py', views.grafico, name='grafico'),
]
