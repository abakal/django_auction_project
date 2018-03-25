# -*- coding: utf-8 -*-
from django.urls import re_path

from auction.lots.views import LotListView,LotDetailView,LotFilterView

urlpatterns = [
        re_path(r'^$', LotListView.as_view(), name='lots'),
        re_path(r'^search/', LotFilterView.as_view(),name='filter'),
        re_path(r'^(?P<slug>[-\w]+)/$',LotDetailView.as_view() , name='lot'),    
]