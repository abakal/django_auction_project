from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from auction.user_profile.forms import SignUpForm
from django.contrib.auth.models import User


# Create your views here.

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if not form.is_valid():
            return render(request,'auth/signup.html',{'form':form})
        else:
            User.objects.create_user(
                    first_name=form.fields['first_name'],
                    username=form.fields['username'],
                    email=form.fields['email'],
                    password=form.fields['password'])
            user=authenticate(username=form.fields['username'],password=form.fields['password'])
            login(request,user)
            return redirect('/')
    else:
        return render(request,'auth/signup.html',{'form':SignUpForm()})
    
            
            