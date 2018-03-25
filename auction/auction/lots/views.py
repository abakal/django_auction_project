from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import  Paginator,EmptyPage,PageNotAnInteger
from auction.lots.models import Lot
from django.views.generic import ListView,DetailView
from auction.lots.filters import LotFilter
from django_filters.views import FilterView
from sorting_bootstrap.views import SimpleChangeList

import random
# Create your views here.

class LotListView(ListView):
    model=Lot
    queryset=Lot.objects.all()
    paginate_by = 2
    context_object_name = 'lots'   
    template_name='lots/lots.html'
    def get_ordering(self):
        ordering = self.request.GET.get('orderby', 'title')
        return ordering
    def get_context_data(self,*args,**kwargs):
        context=super(LotListView,self).get_context_data(*args,**kwargs)
        context['current_order']=self.get_ordering()
        return context
    
    
class LotFilterView(FilterView):
    model=Lot
    template_name='lots/search.html'
    context_object_name = 'lots'
    queryset=Lot.objects.all()
    paginate_by = 1
    filterset_class=LotFilter

    
class LotDetailView(DetailView):
    model = Lot
    template_name='lots/lot.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
