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

    url(r'^article-post/$', views.article_post, name='article_post'),
    url(r'^article-list/$', views.article_list, name='article_list'),
    url(r'^article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)$', views.article_detail, name='article_detail'),

    url(r'^delete-article/$', views.del_article, name='del_article'),
    #url(r'^edit-article/(?P<article_id>\d+)/$', views.edit_article, name="edit_article"),
    path('edit-article/<int:article_id>/', views.edit_article, name="edit_article"),
]
