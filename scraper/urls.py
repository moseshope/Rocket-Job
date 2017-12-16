from django.conf.urls import url
from . import views

app_name = 'scraper'

urlpatterns = [
    url(r'^$', views.ScraperView, name = "aroundtheweb"),
]
