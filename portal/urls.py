from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^formularios/', views.formularios, name='formularios'),
    url(r'^grafico/', views.grafico, name='grafico'),
]
