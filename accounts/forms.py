from django import forms
from .models import Custom_User

from django.shortcuts import render



class Userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model=Custom_User
        fields=['first_name','last_name','username','email','password','confirm_password']
        
        
    def clean(self):
        clean_data=super(Userform,self).clean()
        password=clean_data.get('password')
        confirm_password=clean_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('password Does not match')
          