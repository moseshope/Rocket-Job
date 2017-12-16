from django.conf.urls import url
from . import views

app_name = 'message'

urlpatterns = [

    url(r'^list/(?P<user_id>[0-9]+)/$', views.message, name='message'),

]
