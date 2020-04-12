from django.conf.urls import url
from . import views
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^get_patient_details/$', views.get_patient_details, name='get_patient_details'),
    url(r'^mark_patient_attendance/(?P<pk>[0-9]+)$', csrf_exempt(views.mark_patient_attendance), name='mark_patient_attendance'),
    url(r'^unmark_patient_attendance/(?P<pk>[0-9]+)$', csrf_exempt(views.unmark_patient_attendance),
        name='unmark_patient_attendance'),
    url(r'^show_present_patients/$', views.show_present_patients, name='show_present_patients'),
    url(r'^login/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', PasswordResetView.as_view(template_name='accounts/reset_password.html'),
        name='password_reset'),
    url(r'^reset-password/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset-password/complete/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
