from django import forms
from django.db.models import fields
from django.forms.models import ModelForm
from .models import eventc,EventRegistration,club



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': 'Type your username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Type your username'}))

class RegistrationForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'firstname', 'placeholder': 'Type your firstname'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'lastname', 'placeholder': 'Type your lastname'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'email', 'name': 'email', 'placeholder': 'Type your email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': 'Type your username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Type your password'}))
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'confirm-password', 'placeholder': 'Type your password again'}))




class eventcform(ModelForm):
    class Meta :
        model=eventc
        exclude=('user','status','feedback')
        fields=[ 'title','date','description','place','poster']  
        widgets = {
        'date': forms.DateInput(format=('%Y-%m-%d'), attrs={'placeholder':'Select a date', 'type':'date'}),
    }
   
class EventRegistrationform(ModelForm):
    class Meta:
      model=EventRegistration
      exclude=('user','event')

class clubform(ModelForm):
    class Meta:
        model=club
        fields=['name','about','image']
        exclude=('chef',)