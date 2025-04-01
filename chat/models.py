from django.db import models
from django.utils import timezone

class Message(models.Model):
    """Model representing a chat message"""
    CHATGPT = 'ChatGPT'
    DALLE = 'DALL·E'
    MODEL_CHOICES = [
        (CHATGPT, 'ChatGPT'),
        (DALLE, 'DALL·E'),
    ]
    
    GPT_3_5 = 'gpt-3.5-turbo'
    GPT_4 = 'gpt-4'
    GPT_MODEL_CHOICES = [
        (GPT_3_5, 'GPT-3.5'),
        (GPT_4, 'GPT-4'),
    ]
    
    id = models.AutoField(primary_key=True)
    session_id = models.CharField(max_length=100)
    text = models.TextField()
    ai = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    selected_model = models.CharField(max_length=10, choices=MODEL_CHOICES, default=CHATGPT)
    gpt_version = models.CharField(max_length=20, choices=GPT_MODEL_CHOICES, default=GPT_3_5)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"{self.session_id} - {'AI' if self.ai else 'User'} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class ApiKey(models.Model):
    """Model for storing API keys in the session"""
    session_id = models.CharField(max_length=100, unique=True)
    api_key = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"API Key for {self.session_id}"

