from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings as django_settings
import os
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name='base.html'
    def get(self,request,*args,**kwargs):
        user=request.user
        if user.is_authenticated:
            return redirect('/lots/')
        else:
            return redirect('/login/')