from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, fields

from .models import Work,Comment


class Workform(ModelForm):
    class Meta:
        model = Work
        fields = ['title', 'tags', 'tools_used', 'Cover', 'imageone', 'imagetwo']
        
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
            'tools_used' : forms.CheckboxSelectMultiple()
        }


class Commentform(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        labels = {
            'text': 'Add your comment'
        }
        