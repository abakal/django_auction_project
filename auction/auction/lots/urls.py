# -*- coding: utf-8 -*-
from django.urls import re_path
from auction.lots.views import lots,lot

urlpatterns = [
        re_path(r'^$', lots, name='lots'),
        re_path(r'^(?P<slug>[-\w]+)/$', lot, name='lot'),
    
]
