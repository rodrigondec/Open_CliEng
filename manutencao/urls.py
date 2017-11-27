from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^detalhes/(?P<manutencaoid>\d+)/$', views.manutencao_detalhes, name='manutencao_detalhes'),
]
