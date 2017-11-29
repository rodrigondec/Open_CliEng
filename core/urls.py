from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detalhar_funcionario/(?P<funcionarioid>\d+)/$', views.detalhar_funcionario, name='detalhar_funcionario'),
    url(r'^detalhar_tecnico/(?P<tecnicoid>\d+)/$', views.detalhar_tecnico, name='detalhar_tecnico'),
]
