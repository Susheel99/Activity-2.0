from django import forms
from .models import Account

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        # 'placeholder':'Enter password',
        'class':'form-group form-input',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        # 'placeholder':'confirm password',
        'class':'form-group form-input',
    }))
    class Meta:
        model = Account
        fields = ['first_name','last_name','email','phone_number','password']
    
    def clean(self):
        cleaned_data = super(SignupForm,self).clean()
        password = cleaned_data.get('password')#cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError(
                "password does not match!!."
            )

    def __init__(self,*args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs['placeholder'] = "Enter First name"
        # self.fields['last_name'].widget.attrs['placeholder'] = "Enter Last name"
        # self.fields['phone_number'].widget.attrs['placeholder'] = "Enter Phone Number"
        # self.fields['email'].widget.attrs['placeholder'] = "Enter Email Address"


        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-group form-input'