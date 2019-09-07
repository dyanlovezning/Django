from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.urls import reverse_lazy, path

app_name='article'

urlpatterns = [
    url(r'^article-column/$', views.article_column, name='article_column'),
    url(r'^rename-column/$', views.rename_article_column, name='rename_article_column'),
    url(r'^delete-column/$', views.del_article_column, name='del_article_column'),
]
