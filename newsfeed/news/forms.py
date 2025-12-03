from django import forms
from .models import Contact
from ckeditor.widgets import CKEditorWidget
from .models import News,Comment

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class NewsForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = ['title', 'body','image','category','status']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
