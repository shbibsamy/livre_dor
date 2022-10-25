""" Defines forms """
from django import forms
from .models import Comment

class CommentForm(forms.Form):
    """ Defines form fields """
    email = forms.EmailField(label='Votre email ')
    comment = forms.CharField(label='Votre commentaire ', widget=forms.Textarea, help_text='(Maximum de 400 caractères)')
    
    class Meta:
        """ Defines form model and model fields """
        model = Comment
        fields = ['email', 'comment']