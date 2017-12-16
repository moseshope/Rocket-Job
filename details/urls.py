from django.conf.urls import url
from . import views

app_name = 'details'

urlpatterns = [

    url(r'^job-details/(?P<job_id>[0-9]+)/$', views.job_details, name='job_details'),
    url(r'^job-details/edit-job/(?P<job_id>[0-9]+)/$', views.edit_job, name='edit_job'),
    #url(r'^$', views.job_details, name='job_details'),
    url(r'^job-details/edit-bid/(?P<bid_id>[0-9]+)/$', views.edit_bid, name='edit_bid'),

]
