# todo/forms.py
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        # Bu form ModelForm bo'lib, Todo modeliga asoslanadi
        model = Todo
        
        # Formada qaysi maydonlar ko'rinishi kerakligini belgilaymiz
        fields = ['title', 'priority']
        
        # HTML elementlariga qo'shimcha CSS klasslarini qo'shish uchun
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'todo-input', 
                'placeholder': 'Yangi vazifa qoʻshing...',
                'required': True  # HTML formadagi required atributiga mos
            }),
            'priority': forms.Select(attrs={
                'class': 'todo-input'
            }),
        }