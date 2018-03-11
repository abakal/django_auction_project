"""auction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth.views import login, logout
from django.contrib import admin
from django.urls import path, re_path
from auction.user_profile.views import signup
from auction.core.views import home,settings,profile,picture
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', home, name='home'),
    re_path(r'^settings/$', settings, name='settings'),
    re_path(r'^settings/profile/$', profile, name='profile'),
    re_path(r'^settings/profile/picture/$', picture, name='picture'),
    #re_path(r'^search/$', search, name='search'),
    re_path(r'^signup/$', signup, name='signup'),
    re_path(r'^login', login, {'template_name': 'core/cover.html'}, name='login'),
    re_path(r'^logout', logout, {'next_page': '/'}, name='logout'),
    re_path(r'^lots/', include('auction.lots.urls')),
    
    
]
