
from django.conf.urls import url
from . import views

app_name = 'matching'

urlpatterns = [
    url(r'^map$', views.map, name='map'),
    url(r'^home$', views.home, name='home'),
    url(r'^search$', views.search, name='search'),
    url(r'^login$', views.login, name='login'),
    url(r'^execute_matching$', views.execute_matching, name='execute_matching'),
    url(r'^login_auth$', views.login_auth, name='login_auth'),
    url(r'^register$', views.register, name='register'),
    url(r'^regist_query$', views.regist_query, name='regist_query'),
    url(r'^register_auth$', views.register_auth, name='register_auth'),
    url(r'^matched_but_still_meet$', views.matched_but_still_meet, name='matched_but_still_meet'),
    url(r'^meat_but_still_eval$', views.meat_but_still_eval, name='meat_but_still_eval'),
    ]
