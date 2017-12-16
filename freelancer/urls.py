from django.conf.urls import url
from . import views

app_name = 'freelancer'

urlpatterns = [

    url(r'^$', views.f_home, name='f_home'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^profile/edit-profile/(?P<user_id>[0-9]+)/$', views.edit_profile, name='edit_profile'),


]
