from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.urls import reverse_lazy, path

app_name='account'

urlpatterns = [
    #url(r'^login/$', views.user_login, name="user_login"),
    url(r'^login/$', LoginView.as_view(template_name='registration/login.html'), name="user_login"),
    url(r'^newlogin/$', LoginView.as_view(template_name='account/login.html'), name="user_login"),
    #url(r'^logout/$', LogoutView.as_view(), name="user_logout"),
    url(r'^logout/$', LogoutView.as_view(template_name='account/logout.html'), name="user_logout"),
    url(r'^register/$', views.register, name="user_register"),

    #url(r'^password-change/$', auth_views.password_change, name='password-change'),
    #url(r'^password-change-done/$', auth_views.password_change_done, name='password-change-done'),

    url(r'^password-change/$', auth_views.PasswordChangeView.as_view(template_name='account/password_change_form.html', success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    url(r'^password_change_done/$', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name='password_change_done'),
    #path('password-change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html',success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    #path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),

    url(r'^password-reset/$', auth_views.PasswordResetView.as_view(
        template_name='account/password_reset_form.html', 
        email_template_name='account/password_reset_email.html',
        subject_template_name='account/password_reset_subject.txt',
        success_url=reverse_lazy('account:password_reset_done')), name='password_reset'),
    url(r'^password-reset-done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='account/password_reset_done.html'), name='password_reset_done'),
    url(r'^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)    /$', auth_views.PasswordResetConfirmView.as_view(
        template_name='account/password_reset_confirm.html',
        success_url=reverse_lazy('account:password_reset_complete')), name='password_reset_confirm'),
    url(r'^password-reset-complete/$', auth_views.PasswordResetCompleteView.as_view(
        template_name='account/password_reset_complete.html'), name='password_reset_complete'),


    url(r'^my-information/$', views.myself, name="my_information"),
    url(r'^edit-my-information/$', views.myself_edit, name="edit_my_information"),
]
