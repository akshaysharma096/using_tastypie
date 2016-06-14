"""using_tastypie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from tastypie.api import Api
from django.conf.urls import url, include
from user.api import EntryResource

entry_resource = EntryResource()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^blog/', include('user.urls')),
    url(r'^api/', include(entry_resource.urls)),
]
