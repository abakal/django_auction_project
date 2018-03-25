from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime
from django.template.defaultfilters import slugify

# Create your models here.

class Lot(models.Model):
    OPEN='FR'
    CLOSED='CL'
    CANCELLED='CN'
    STATUS=(
            (OPEN,'Open'),
            (CLOSED,'Closed'),
            (CANCELLED,'Cancelled')
            )
    
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    picture = models.ImageField(blank=True)
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateTimeField(blank=True)
    status=models.CharField(max_length=2,choices=STATUS,default=OPEN)
    winner=models.ForeignKey(User,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=255,null=True,blank=True)
    
    class Meta:
        db_table='"lots"'
        verbose_name=_(u'Lot')
        verbose_name_plural=_(u'Lots')
        ordering=('-start_date','end_date','winner')
    def __unicode__(self):
        return self.title
    @staticmethod
    def get_opened():
        lots = Lot.objects.filter(status=Lot.OPEN)
        return lots
     
    
class Bet(models.Model):
    bet_user=models.ForeignKey(User,on_delete=models.CASCADE)
    lot=models.ForeignKey(Lot,on_delete=models.CASCADE)
    bet_time=models.TimeField(auto_now_add=True)
    sum_bet=models.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
        db_table='"Bets"'
        verbose_name=_(u'Bet')
        verbose_name_plural=_(u'Bets')
        ordering=('bet_user','-bet_time',)
    def __unicode__(self):
        return self.title
        
        
    
    
    
    
    


