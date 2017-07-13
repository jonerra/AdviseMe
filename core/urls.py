from django.conf.urls import include, url
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^user/', include('registration.backends.simple.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
    url(r'^login$', auth_views.login, name='login'),
]