from django import forms
from .models import Manager

class ManagerForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'uk-input uk-form-success uk-form-width-large'}))
    contact_no = forms.CharField(widget=forms.TextInput(attrs={'class':'uk-input uk-form-success uk-form-width-large'}))
    designation = forms.CharField(widget=forms.TextInput(attrs={'class':'uk-input uk-form-success uk-form-width-large'}))

    class Meta:
        model = Manager
        exclude = ('image','user')