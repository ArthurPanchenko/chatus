from django import forms

from .models import Chat


class CreateChatForm(forms.ModelForm):
    
    class Meta:
        model = Chat
        fields = (
            'title',
            'participants'
        )

