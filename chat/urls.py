from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('send_message/', views.send_message, name='send_message'),
    path('clear_chat/', views.clear_chat, name='clear_chat'),
    path('save_api_key/', views.save_api_key, name='save_api_key'),
    path('remove_api_key/', views.remove_api_key, name='remove_api_key'),
    path('check_api_key/', views.check_api_key_view, name='check_api_key'),
    path('toggle_theme/', views.toggle_theme, name='toggle_theme'),
]

