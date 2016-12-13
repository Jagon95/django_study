from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'logsys'

urlpatterns = [
    # ex: /polls/
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^logout/$', views.LogOutView.as_view(), name='logout'),
    # url(r'^signup/$', 'django.contrib.auth.views.logout', {'next_page': 'logsys:login'}, name='logout'),
    url(r'^user/$', views.HomePageView.as_view(), name='user'),
    url(r'^useredit/$', views.update_profile, name='useredit'),
    url(r'^home/$', TemplateView.as_view(template_name="logsys/home.html"), name='home')
]
