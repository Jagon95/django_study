from django.conf.urls import url

from . import views

app_name = 'logsys'

urlpatterns = [
    # ex: /polls/
    url(r'^login/$', views.LoginView.as_view(), name='index'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^user/$', views.HomePageView.as_view(), name='user'),
]
