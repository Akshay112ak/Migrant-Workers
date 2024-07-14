from django import forms
from . model15 import Home15


class login4(forms.ModelForm):
    class Meta:
        model=Home15
        fields=['email','password']
        Widgets={
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }