from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model,aauthenticate
from django.utils.html import strip_tags
from django.core.validators import RegexValidator


User=get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=66,widget=forms.EmailInput(attrs={'class':'form-control inter-register','placeholder':'Email'}))
    first_name = forms.CharField(required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control inter-register','placeholder':'First Name'}))
    last_name = forms.CharField(required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control inter-register','placeholder':'Last Name'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control inter-register','placeholder':'Password'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control inter-register','placeholder':'Confirm Password'}))
    phone_number = forms.CharField(required=False, max_length=20,widget=forms.TextInput(attrs={'class':'form-control inter-register','placeholder':'Phone Number'}), validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number.')])    
    marketing_consent1 = forms.BooleanField(required=False, label="I agree to receive commerscial,promotion",widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    marketing_consent2 = forms.BooleanField(required=False, label="I agree to the privacy policy",widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))


    class Meta:
        model=User
        fields=('email','first_name','last_name','password1','password2','phone_number','marketing_consent1','marketing_consent2')

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email
    
    def save(self, commit =True):
        user=super().save(commit=False)
        user.username=None
        user.marketing_consent1=self.cleaned_data.get('marketing_consent1')
        user.marketing_consent2=self.cleaned_data.get('marketing_consent2')
        if commit:
            user.save()
        return user
    


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(required=True, max_length=66,label="Email",widget=forms.EmailInput(attrs={'class':'form-control inter-login','placeholder':'Email','autofocus':True}))   
    