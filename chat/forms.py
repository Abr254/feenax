# chat/forms.py

from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']  # Only ask for the text message
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': ' message ...'}),
        }

    # Optionally, you can add custom validation or methods if needed
    def clean_text(self):
        text = self.cleaned_data.get('text')
        if not text:
            raise forms.ValidationError("Message text cannot be empty")
        return text