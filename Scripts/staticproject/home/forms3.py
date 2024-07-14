from django import forms
from . model17 import Home17
class labchating(forms.ModelForm):
    class Meta:
        model=Home17
        fields=['message']
        widgets={
            'message':forms.TextInput(attrs={'class':'form-control'}),
            
        }
