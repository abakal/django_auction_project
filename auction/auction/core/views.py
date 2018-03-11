from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from auction.core.forms import ProfileForm
from django.contrib import messages
from django.conf import settings as django_settings
import os
# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@login_required
def settings(request):
    user = request.user
    return render(request, 'core/activity.html')

@login_required
def profile(request):
    user=request.user
    if request.method=='POST':
        form=ProfileForm(request.POST)
        if form.is_valid():
            user.first_name=form.cleaned_data.get('first_name')
            user.email=form.cleaned_data.get('email')
            user.save()
            messages.add_message(request,messages.SUCCES, '')
    else:
        form=ProfileForm(instance=user,initial={
                'email':user.email
                })
    return render(request,'core/profile.html',{'form':form})

@login_required
def picture(request):
    uploaded_picture = False
    try:
        if request.GET.get('upload_picture') == 'uploaded':
            uploaded_picture = True
    except Exception as e:
        pass
    return render(request, 'core/picture.html', {'uploaded_picture': uploaded_picture})    
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