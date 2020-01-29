from django import forms
from Account.models import Account


class TeacherSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Teacher's email address"}), label="")
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Give an username"}), label="")

    class Meta:
        model = Account
        fields = ['email', 'username',]