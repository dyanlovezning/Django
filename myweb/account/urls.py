from django.conf.urls import url
from . import views
from django.conf import settings
app_name='account'

urlpatterns = [
    url(r'^login/$', views.user_login, name="user_login"),
]