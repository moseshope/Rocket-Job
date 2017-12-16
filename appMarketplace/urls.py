from django.conf.urls import url
from . import views

app_name = 'appMarketplace'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact_us, name='contact_us'),
]
