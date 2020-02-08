from django import forms
from .models import Class

class ClassForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'uk-input uk-form-success uk-form-width-large'}))
    section = forms.CharField(widget=forms.TextInput(attrs={'class':'uk-input uk-form-success uk-form-width-large'}),required=False)
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'uk-input uk-form-success uk-form-width-large'}),required=False)

    class Meta:
        model = Class
        exclude = ('code','teacher')

