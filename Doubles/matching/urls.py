
from django.conf.urls import url
from . import views

app_name = 'matching'

urlpatterns = [
    url(r'^matching$', views.map, name='map'),
    ]
