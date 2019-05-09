from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^read/$', views.read, name='read'),
    url(r'^read/(?P<id>\d+)/$', views.read_detail, name='read_detail'),
    url(r'^daftar/$', views.daftar, name='daftar'),
    url(r'^profile/$', views.view_profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^login/$', login, {'template_name': 'login.html'}),
    url(r'^logout/$', logout, {'template_name': 'logout.html'}),
    url(r'^tentang/$', views.tentang, name='tentang'),
    url(r'^bukukkn/$', views.bukukkn, name='bukukkn'),
    url(r'^riset/$', views.riset, name='riset'),
    url(r'^prosiding/$', views.prosiding, name='prosiding')
    
]