from django import forms
from .models import Note
from django.core.exceptions import ValidationError


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note

        fields = [
            'title',
            'content',
        ]

        help_texts = {
            'title': 'Note title',
            'content': 'Note content'
        }

        error_messages = {
            'title': {
                'required': 'This field is required'
            }
        }