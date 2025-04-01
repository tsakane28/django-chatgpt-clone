from django.contrib import admin
from .models import Message, ApiKey

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'session_id', 'ai', 'selected_model', 'created_at')
    list_filter = ('ai', 'selected_model', 'gpt_version')
    search_fields = ('session_id', 'text')
    date_hierarchy = 'created_at'

@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'created_at')
    search_fields = ('session_id',)

