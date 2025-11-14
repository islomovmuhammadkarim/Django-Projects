from django import forms
from .models import ContactMessage,Todo


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }
        

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'deadline']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Vazifa nomi'}),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
