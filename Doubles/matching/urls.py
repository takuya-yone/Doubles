
from django.conf.urls import url
from . import views

app_name = 'matching'

urlpatterns = [
    url(r'^map$', views.map, name='map'),
    url(r'^search$', views.search, name='search'),
    ]
