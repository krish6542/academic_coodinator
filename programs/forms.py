from django import forms
from .models import Program


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['title', 'description', 'program_type', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input w-full', 'placeholder': 'Program title'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea w-full', 'rows': 3, 'placeholder': 'Short description'}),
            'program_type': forms.Select(attrs={'class': 'form-select w-full'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
