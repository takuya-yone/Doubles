
from django.conf.urls import url
from . import views

app_name = 'matching'

urlpatterns = [
    url(r'^map$', views.map, name='map'),
    url(r'^search$', views.search, name='search'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^register_auth$', views.register_auth, name='register_auth'),
    ]
