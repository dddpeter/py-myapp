"""data_importer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib.auth import views
from views import api_views
from views import information_views

urlpatterns = [
    # Front end
    url(r'^$', api_views.index, name='index'),
    # CYG APIs
    url(r'^api/organ$', api_views.organ, name='organ_import'),
    url(r'^api/user$', api_views.user, name='user_import'),
    url(r'^api/activity$', api_views.activity, name='activity_import'),
    url(r'^api/user_activity$', api_views.user_activity, name='user_activity_import'),
    url(r'^api/user_organ$', api_views.user_organ, name='user_organ_import'),

    # Administrator
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login, {'template_name': 'admin/login.html'})
]
