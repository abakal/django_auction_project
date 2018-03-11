from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    url=models.CharField(max_length=500,null=True,blank=True)
    picture=models.ImageField(default=None)
    money_earned=models.FloatField(default=500.00)
    
    class Meta:
        db_table='"user_profiles"'
#    def get_activity(self):
#        activity=[]
    def get_url(self):
        url = self.url
        if "http://" not in self.url and "https://" not in self.url and len(self.url) > 0:
            url = "http://" + str(self.url)
        return url
    def get_picture(self):
        return self.url or 'https://qsf.is.quoracdn.net/-72c091d25b3e045b.png'
#Теперь добавим немножко магии: определим сигналы, чтобы наша модель Profile автоматически обновлялась при создании/изменении данных модели User.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)        
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
#Мы «зацепили» create_user_profile() и save_user_profile() к событию сохранения модели User. Такой сигнал называется post_save.