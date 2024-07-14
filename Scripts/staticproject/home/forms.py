from datetime import date
import datetime
import re  # For regular expressions
#from django.contrib.auth.forms import Password
from django.core.exceptions import ValidationError
from django import forms
from . models import Home
from . model1 import Home1
from . model2 import Home2
from . model3 import Home3
from . model4 import NOTI
from . model5 import SCHOME
from . model6 import COMP
from . model7 import Home7
from . model8 import Home8
from . model9 import Home9
from . model12 import Home12
from . model13 import Home13
from . model14 import Home14
from . model17 import Home17
from . model18 import Home18

class students(forms.ModelForm):
    class Meta:
        model=Home
        fields=['agencyname','address','pincode','district','city','agencyid','contactnumber','email','password']
        widgets={
            'agencyname':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'pincode':forms.TextInput(attrs={'class':'form-control'}),
            'district':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'agencyid':forms.TextInput(attrs={'class':'form-control'}),
            'contactnumber':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }
    def clean_contact(self):
        contactnumber = str(self.cleaned_data['contactnumber'])
        if not re.match(r'^\d{10}$', contactnumber):
            raise ValidationError("Invalid contact number. Please enter a 10-digit phone number.")
        return contactnumber

    def clean_contactnumber(self):
        contactnumber = str(self.cleaned_data.get('contactnumber', ''))  # Convert to string
        if not re.match(r'^\d{10}$', contactnumber):
            raise forms.ValidationError("Invalid contact number. Please enter a 10-digit phone number.")
        return contactnumber

    
    def clean_pincode(self):
        pincode = str(self.cleaned_data['pincode'])  # Convert to string
        if not (len(pincode) == 6 or len(pincode) == 7) or not pincode.isdigit():
            raise ValidationError("Invalid pincode. Please enter a 6 or 7-digit number.")
        return pincode
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least one digit.")
        if not any(char.isalpha() for char in password):
            raise ValidationError("Password must contain at least one letter.")
        return password
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs.get('instance'):
            self.fields['email'].widget.attrs['readonly'] = True
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if Home.objects.filter(email=email).exists():
    #         raise ValidationError("This email address is already registered.")
    #     return email
        
class worker(forms.ModelForm):
    class Meta:
        model=Home1
        fields=['workername','address','pincode','state','district','city','aadharnumber','contactnumber','email','password']
        widgets={
            'workername':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'pincode':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'district':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'aadharnumber':forms.TextInput(attrs={'class':'form-control'}),
            'contactnumber':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            
        }
    def clean_contactnumber(self):
        contactnumber = str(self.cleaned_data.get('contactnumber', ''))  # Convert to string
        if not re.match(r'^\d{10}$', contactnumber):
            raise forms.ValidationError("Invalid contact number. Please enter a 10-digit phone number.")
        return contactnumber
    def clean_aadharnumber(self):
        aadharnumber = str(self.cleaned_data.get('aadharnumber', ''))  # Convert to string
        if not re.match(r'^\d{12}$', aadharnumber):
            raise forms.ValidationError("Invalid aadharnumber . Please enter a 12-digit aadharnumber .")
        return aadharnumber

    
    def clean_pincode(self):
        pincode = str(self.cleaned_data['pincode'])  # Convert to string
        if not (len(pincode) == 6 or len(pincode) == 7) or not pincode.isdigit():
            raise ValidationError("Invalid pincode. Please enter a 6 or 7-digit number.")
        return pincode
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least one digit.")
        if not any(char.isalpha() for char in password):
            raise ValidationError("Password must contain at least one letter.")
        return password
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs.get('instance'):
            self.fields['email'].widget.attrs['readonly'] = True
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if Home1.objects.filter(email=email).exists():
    #         raise ValidationError("This email address is already registered.")
    #     return email
class police(forms.ModelForm):
    class Meta:
        model=Home2
        fields=['stationid','addressline1','addressline2','pincode','state','district','city','contactnumber','email','password']
        widgets={
            'stationid':forms.TextInput(attrs={'class':'form-control'}),
            'addressline1':forms.Textarea(attrs={'class':'form-control'}),
            'addressline2':forms.Textarea(attrs={'class':'form-control'}),
            'pincode':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'district':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'contactnumber':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            
        }
    def clean_contactnumber(self):
        
        contactnumber1 = str(self.cleaned_data.get('contactnumber', ''))  # Convert to string
        if not re.match(r'^\d{10}$', contactnumber1):
            print("Invalid contact number. Please enter a 10-digit phone number.")
            raise forms.ValidationError("Invalid contact number. Please enter a 10-digit phone number.")
        return contactnumber1

    
    def clean_pincode(self):
        
        pincode1 = str(self.cleaned_data['pincode'])  # Convert to string
        if not (len(pincode1) == 6 or len(pincode1) == 7) or not pincode1.isdigit():
            raise ValidationError("Invalid pincode. Please enter a 6 or 7-digit number.")
        return pincode1
    
    def clean_password(self):
        
        password1 = self.cleaned_data.get('password')
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password1):
            raise ValidationError("Password must contain at least one digit.")
        if not any(char.isalpha() for char in password1):
            raise ValidationError("Password must contain at least one letter.")
        return password1
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if Home2.objects.filter(email=email).exists():
    #         raise ValidationError("This email address is already registered.")
        return email
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs.get('instance'):
            self.fields['email'].widget.attrs['readonly'] = True
class insage(forms.ModelForm):
    class Meta:
        model=Home3
        fields=['agencyname','state','district','contactnumber','regid','email','password']
        widgets={
            'agencyname':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'district':forms.TextInput(attrs={'class':'form-control'}),
            'contactnumber':forms.TextInput(attrs={'class':'form-control'}),
            'regid':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            
        }
    def clean_contactnumber(self):
        
        contactnumber1 = str(self.cleaned_data.get('contactnumber', ''))  # Convert to string
        if not re.match(r'^\d{10}$', contactnumber1):
            print("Invalid contact number. Please enter a 10-digit phone number.")
            raise forms.ValidationError("Invalid contact number. Please enter a 10-digit phone number.")
        return contactnumber1
    def clean_password(self):
        
        password1 = self.cleaned_data.get('password')
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password1):
            raise ValidationError("Password must contain at least one digit.")
        if not any(char.isalpha() for char in password1):
            raise ValidationError("Password must contain at least one letter.")
        return password1
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if Home3.objects.filter(email=email).exists():
    #         raise ValidationError("This email address is already registered.")
    #     return email
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs.get('instance'):
            self.fields['email'].widget.attrs['readonly'] = True

class noti(forms.ModelForm):
    class Meta:
        model=NOTI
        fields=['NOTIFICATION']
        widgets={
            'NOTIFICATION':forms.Textarea(attrs={'class':'form-control'}),
            
            
        }
class schome(forms.ModelForm):
    class Meta:
        model=SCHOME
        fields=['SCHEME_TYPE','SCHEME_NAME','SCHEME_AMOUNT','MONTHLY_AMOUNT','INTEREST_RATE','SCHEME_DETAILS']
        widgets={
            'SCHEME_TYPE':forms.TextInput(attrs={'class':'form-control'}),
            'SCHEME_NAME':forms.TextInput(attrs={'class':'form-control'}),
            'SCHEME_AMOUNT':forms.TextInput(attrs={'class':'form-control'}),
            'MONTHLY_AMOUNT':forms.TextInput(attrs={'class':'form-control'}),
            'INTEREST_RATE':forms.TextInput(attrs={'class':'form-control'}),
            'SCHEME_DETAILS':forms.Textarea(attrs={'class':'form-control'}),
        }
class comp(forms.ModelForm):
    class Meta:
        model=COMP
        fields=['COMPLAINT_SUBJECT','COMPLAINT']
        widgets={
            'COMPLAINT_SUBJECT':forms.TextInput(attrs={'class':'form-control'}),
            'COMPLAINT':forms.Textarea(attrs={'class':'form-control'}),
            
            
        }
class woratt(forms.ModelForm):
    class Meta:
        model=Home7
        fields=['ATTENDANCE']
        Widgets={
            'ATTENDANCE':forms.RadioSelect,
        }
class salaryage(forms.ModelForm):
    class Meta:
      model=Home8
      fields=['JOB_CATEGORY','SALARY_PER_DAY']
      widgets={
          'ATTENDANCE':forms.RadioSelect,
          'SALARY_PER_DAY':forms.TextInput(attrs={'class':'form-control'}),
          
      }
class assaignwork(forms.ModelForm):
    class Meta:
      model=Home9
      fields=['JOB_CATEGORY','Working_place']
      widgets={
          'JOB_CATEGORY': forms.Select(attrs={'class': 'form-control'}),
          'Working_place':forms.TextInput(attrs={'class':'form-control'}),
          
        } 
    def clean_Working_place(self):
        working_place = self.cleaned_data.get('Working_place')

        # Check if Working_place is an integer
        if not working_place.isdigit():
            raise ValidationError("Working place must be a valid integer (pin code).")

        # Check if the length of the pin code is either 6 or 7 digits
        if len(working_place) not in (5, 7):
            raise ValidationError("Pin code must be 5 or 7 digits long.")

        return working_place     
class reportpolice(forms.ModelForm):
    class Meta:
        model=Home12
        fields=['file']
class insuranceworker(forms.ModelForm):
    class Meta:
        model=Home13
        fields=['file']
class paymentinsurance(forms.ModelForm):
    class Meta:
        model=Home14
        fields=['Nameoncard','Cardnumber','CVV','Expiredate']
        widgets={
            'Nameoncard':forms.TextInput(attrs={'class':'form-control'}),
            'Cardnumber':forms.TextInput(attrs={'class':'form-control'}),
            'CVV':forms.TextInput(attrs={'class':'form-control'}),
            'Expiredate':forms.TextInput(attrs={'class':'form-control'}),
        }
    def clean_Cardnumber(self):
        Cardnumber = str(self.cleaned_data.get('Cardnumber', ''))  # Convert to string
        if not re.match(r'^\d{16}$', Cardnumber):
            raise forms.ValidationError("Invalid Cardnumber . Please enter a 16-digit Cardnumber .")
        return Cardnumber
    def clean_CVV(self):
        CVV = str(self.cleaned_data.get('CVV', ''))  # Convert to string
        if not re.match(r'^\d{3}$', CVV):
            raise forms.ValidationError("Invalid CVV . Please enter a 03-digit CVV .")
        return CVV
    def clean_Expiredate(self):
        Expiredate = str(self.cleaned_data.get('Expiredate', ''))
        if not re.match(r'^(0[1-9]|1[0-2])/\d{2}$', Expiredate):
            raise forms.ValidationError("Invalid expiry date. Please use the format 'mm/yy'.")
        return Expiredate
class cardupload(forms.ModelForm):
    class Meta:
        model=Home18
        fields=['file']
        
            
            
            
        


      

      