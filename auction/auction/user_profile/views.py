from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login
from auction.user_profile.forms import SignUpForm,ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings as django_settings
from django.views import View

class SignUpView(View):
    form_class=SignUpForm
    initial={'form':SignUpForm()}
    template_name='auth/signup.html'
    def get(self,request,*args,**kwargs):
        form=self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if not form.is_valid():
            return render(request,self.template_name,{'form':form})
        else:
            form.save()
            firstname=form.fields['firstname']
            username=form.fields['username']
            email=form.fields['email']
            password=form.fields['password']
            user=authenticate(username=form.fields['username'],password=form.fields['password'])
            login(self.request,user)
            return redirect('/')
                
class Settings(View):
    template_name='auth/activity.html'
    def get(self,request,*args,**kwars):
        user=request.user
        return render(request,self.template_name)

#@login_required
#def profile(request):
#    user=request.user
#    if request.method=='POST':
#        form=ProfileForm(request.POST)
#        if form.is_valid():
#            user.first_name=form.cleaned_data.get('first_name')
#            user.email=form.cleaned_data.get('email')
#            user.save()
#            messages.add_message(request,messages.SUCCES, '')
#    else:
#        form=ProfileForm(instance=user,initial={
#                'email':user.email
#                })
#    return render(request,'auth/profile.html',{'form':form})

class Profile(View):
    form_class=ProfileForm
    template_name='auth/profile.html'
    def get(self,request,*args,**kwargs):
        user=self.request.user
        form=self.form_class(instance=user,initial={'email':user.email})        
        return render(request,self.template_name,{'form':form})
    def post(self,request,*args,**kwargs):
        user=self.request.user
        form=self.form_class(request.POST)
        if not form.is_valid():
            return render(request,self.template_name,{'form':form})
        else:
            user.first_name=form.cleaned_data.get('firstname')
            user.email=form.cleaned_data.get('email')
            user.save()
            messages.add_message(request,messages.SUCCESS, 'Your profile were successfully edited.')
        return render(request,self.template_name,{'form':form},messages)
        

@login_required
def picture(request):
    uploaded_picture = False
    try:
        if request.GET.get('upload_picture') == 'uploaded':
            uploaded_picture = True
    except Exception as e:
        pass
    return render(request, 'auth/picture.html', {'uploaded_picture': uploaded_picture})

@login_required
def upload_picture(request):
    pass

@login_required
def save_uploaded_picture(request):
    try:
        x = int(request.POST.get('x'))
        y = int(request.POST.get('y'))
        w = int(request.POST.get('w'))
        h = int(request.POST.get('h'))
        tmp_filename = django_settings.MEDIA_ROOT + '/profile_pictures/' + request.user.username + '_tmp.jpg'
        filename = django_settings.MEDIA_ROOT + '/profile_pictures/' + request.user.username + '.jpg'
        im = Image.open(tmp_filename)
        cropped_im = im.crop((x, y, w+x, h+y))
        cropped_im.thumbnail((200, 200), Image.ANTIALIAS)
        cropped_im.save(filename)
        os.remove(tmp_filename)
    except Exception as e:
        pass
    return redirect('/settings/picture/')           