from django.conf.urls import url
from . import views

app_name = 'employee'

urlpatterns = [

    url(r'^$', views.e_home, name='e_home'),
    url(r'^add-job/$', views.add_job, name='add_job'),
#    url(r'^edit-job/$', views.edit_job, name='edit_job'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^profile/edit-profile/(?P<user_id>[0-9]+)/$', views.edit_profile, name='edit_profile'),

]
