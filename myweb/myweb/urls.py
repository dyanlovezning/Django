"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'blog/', include(('blog.urls', 'blog'), namespace='blog')),
    url(r'account/', include(('account.urls', 'account'), namespace='account')),
    url(r'pwd-reset/', include(('password_reset.urls', 'password_reset'), namespace='password_reset')),
    url(r'article/', include(('article.urls', 'article'), namespace='article')),
    url(r'home/', TemplateView.as_view(template_name='home.html'), name='home'),
]
