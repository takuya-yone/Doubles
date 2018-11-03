
from django.conf.urls import url
from . import views

app_name = 'waiting'

urlpatterns = [
    url(r'^waiting$', views.waiting, name='waiting'),
    url(r'^matching_for_other$', views.matching_for_other, name='matching_for_other'),
    ]
