from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import  Paginator,EmptyPage,PageNotAnInteger
from auction.lots.models import Lot

# Create your views here.


def _lots(request,lots):
    paginator=Paginator(lots,10)
    page = request.GET.get('page')
    try:
        lots=paginator.page(page)
    except PageNotAnInteger:
        lots=paginator.page(1)
    except EmptyPage:
        lots=paginator.page(paginator.num_pages)
    return render(
            request,
            'lots/lots.html',
            {'lots':lots,})
    
def lots(request):
    all_lots = Lot.get_published()
    return _lots(request, all_lots)
def lot(request, slug):
    lot = get_object_or_404(Lot, slug=slug, status=Lot.OPEN)
    return render(request, 'lots/lot.html', {'lot': lot})