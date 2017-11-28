from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detalhes/(?P<manutencaoid>\d+)/$', views.manutencao_detalhes, name='manutencao_detalhes'),
]
