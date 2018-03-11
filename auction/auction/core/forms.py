from django import forms
from django.contrib.auth.models import User

# -*- coding: utf-8 -*-
class ProfileForm(forms.ModelForm):
    firstname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
                              max_length=30,
                              required=True)
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
                          max_length=75,
                          required=False)
    class Meta:
        model=User
        fields=['first_name','email']
    
