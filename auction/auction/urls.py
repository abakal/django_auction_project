from django.contrib.auth.views import login, logout
from django.contrib import admin
from django.urls import path, re_path
from auction.user_profile.views import picture,save_uploaded_picture#signup,settings,profile,
from django.conf.urls import include
from django.conf.urls.static import static
from auction.user_profile.views import SignUpView,Settings,Profile
from auction.core.views import HomeView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'^settings/$', login_required(Settings.as_view()), name='settings'),
    re_path(r'^settings/profile/$', login_required(Profile.as_view()), name='profile'),
    re_path(r'^settings/picture/$', picture, name='upload_picture'),
    re_path(r'^settings/picture/save_uploaded_picture/$',save_uploaded_picture, name='save_uploaded_picture'),
    #re_path(r'^search/$', search, name='search'),
    re_path(r'^signup/$',SignUpView.as_view(), name='signup'),
    re_path(r'^login', login, {'template_name': 'auth/login.html'}, name='login'),
    re_path(r'^logout', logout, {'next_page': '/'}, name='logout'),
    re_path(r'^lots/', include('auction.lots.urls')),
       
]
