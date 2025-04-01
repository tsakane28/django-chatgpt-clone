from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    """Form for creating a new message"""
    class Meta:
        model = Message
        fields = ['text', 'selected_model', 'gpt_version']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'w-full grow input input-bordered max-h-[20rem] min-h-[3rem]',
                'placeholder': 'Type your message here...',
                'rows': 1,
            }),
            'selected_model': forms.Select(attrs={
                'class': 'w-full sm:w-40 select select-bordered join-item',
            }),
            'gpt_version': forms.Select(attrs={
                'class': 'tab',
            }),
        }

class ApiKeyForm(forms.Form):
    """Form for setting the OpenAI API key"""
    api_key = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full max-w-xs input input-bordered',
            'placeholder': 'Enter your OpenAI API key',
        }),
        required=True
    )

