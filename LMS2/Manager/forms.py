from django import forms
from Account.models import Account


class TeacherSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Teacher's email address"}), label="")

    class Meta:
        model = Account
        fields = ['email',]