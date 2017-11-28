from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detalhar/(?P<equipamentoid>\d+)/$', views.detalhar, name='equipamento_detalhes'),
    url(r'^detalhar_contrato/(?P<contratoid>\d+)/$', views.detalhar_contrato, name='contrato_detalhes'),
]
