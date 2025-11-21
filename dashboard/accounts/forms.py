from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm

# Ro'yxatdan o'tish
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email allaqachon ishlatilgan")
        return email

# Login
class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")

# Password reset
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email", max_length=254)

# Password set (reset keyin)
class CustomSetPasswordForm(SetPasswordForm):
    pass
