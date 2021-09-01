from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, fields

from .models import Work

class Workform(ModelForm):
    class Meta:
        model = Work
        fields = ['title', 'tags', 'tools_used', 'Cover']
        
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
            'tools_used' : forms.CheckboxSelectMultiple()
        }

        