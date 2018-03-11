from django.contrib import admin
from auction.lots.models import Lot,Bet
# Register your models here.


class LotAdmin(admin.ModelAdmin):
    list_display=('title',
                  'description',
                  'picture',
                  'start_date',
                  'end_date',
                  'status',
                  'winner',
                  'slug')
    
admin.site.register(Lot,LotAdmin)
    
    
        