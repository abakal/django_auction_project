from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class SignUpForm(forms.ModelForm):
    firstname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
                               max_length=30,
                               required=True,
                               label=_(u'First name'),)
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
                               max_length=30,
                               required=True,
                               label=_(u'Username'),)
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}),
                               max_length=30,
                               required=True,
                               label=_(u'E-mail'),)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),
                             label=_(u'Password'))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),
                             label=_(u'Confirm password'))
    class Meta:
        model = User
        fields = [ 'username', 'password','email']
        
    def clean(self):
        cleaned_data=super(SignUpForm,self).clean()
        firstname=cleaned_data.get('firstname')
        username=cleaned_data.get('username')
        email=cleaned_data.get('email')
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        
        if password!=confirm_password:
            raise forms.ValidationError(
                    'Password and Confirm password does not match')
        
        