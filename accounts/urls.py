from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [

    url(r'^login/$', views.login_view, name="login"),
#    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login_form.html'}, name="login"),
#    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name="logout"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/accounts/login/'}, name="logout"),
    url(r'^employeesignup/$', views.SignUpViewE, name="e_reg"),
    url(r'^freelancersignup/$', views.SignUpViewF, name="f_reg"),
#    url(r'^freelancersignup/$', views.UserFormView.as_view(), name="f_reg"),

]
