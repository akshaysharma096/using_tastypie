# urls.py
from django.conf.urls import include, url
from .views import LoginView
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import *
from django.conf.urls import (
handler400, handler403, handler404, handler500
)

urlpatterns=[
	url(r'^login/$',LoginView.as_view(),name='Login'),			#overriding class attribute 
]