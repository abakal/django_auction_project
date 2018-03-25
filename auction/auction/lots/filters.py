from auction.lots.models import Lot
from django_filters import FilterSet,CharFilter
from django.db import models

class LotFilter(FilterSet):
    class Meta:
        model = Lot
        fields = ['title','start_date', 'winner', ]
        
        filter_overrides = {
             models.CharField: {
                 'filter_class': CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
            }