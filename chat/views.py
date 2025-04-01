import json
import uuid
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from .models import Message, ApiKey
from .forms import MessageForm, ApiKeyForm
from .utils import (
    check_api_key, 
    clean_prompt, 
    generate_chatgpt_response, 
    generate_dalle_image
)

def get_session_id(request):
    """Get or create a session ID for the current user"""
    if not request.session.get('session_id'):
        request.session['session_id'] = str(uuid.uuid4())
    return request.session['session_id']

def index(request):
    """Main view for the chat application"""
    session_id = get_session_id(request)
    
    # Get messages for this session
    messages = Message.objects.filter(session_id=session_id)
    
    # Check if API key exists for this session
    api_key_exists = ApiKey.objects.filter(session_id=session_id).exists()
    
    # Get theme preference
    theme = request.session.get('theme', 'dark')
    
    # Create forms
    message_form = MessageForm()
    api_key_form = ApiKeyForm()
    
    # Template suggestions
    template_suggestions = [
        {"title": "Plan a trip", "prompt": "I want to plan a trip to New York City."},
        {"title": "how to make a cake", "prompt": "How to make a cake with chocolate and strawberries?"},
        {"title": "Business ideas", "prompt": "Generate 5 business ideas for a new startup company."},
        {"title": "What is recursion?", "prompt": "What is recursion? show me an example in python."},
    ]
    
    context = {
        'messages': messages,
        'message_form': message_form,
        'api_key_form': api_key_form,
        'api_key_exists': api_key_exists,
        'theme': theme,
        'template_suggestions': template_suggestions,
    }
    
    return render(request, 'chat/index.html', context)

@require_POST
def send_message(request):
    """Handle sending a message and getting a response"""
    session_id = get_session_id(request)
    
    # Check if API key exists
    try:
        api_key_obj = ApiKey.objects.get(session_id=session_id)
        api_key = api_key_obj.api_key
    except ApiKey.DoesNotExist:
        return JsonResponse({'error': 'API key not found'}, status=400)
    
    # Get form data
    form = MessageForm(request.POST)
    
    if form.is_valid():
        # Create user message
        user_message = form.save(commit=False)
        user_message.session_id = session_id
        user_message.ai = False
        user_message.text = clean_prompt(user_message.text)
        user_message.save()
        
        # Generate AI response
        try:
            if user_message.selected_model == 'ChatGPT':
                ai_response = generate_chatgpt_response(
                    user_message.text, 
                    api_key, 
                    user_message.gpt_version
                )
            else:  # DALL-E
                ai_response = generate_dalle_image(user_message.text, api_key)
            
            # Save AI response
            ai_message = Message(
                session_id=session_id,
                text=ai_response,
                ai=True,
                selected_model=user_message.selected_model,
                gpt_version=user_message.gpt_version
            )
            ai_message.save()
            
            return JsonResponse({
                'status': 'success',
                'user_message': {
                    'id': user_message.id,
                    'text': user_message.text,
                    'ai': False,
                    'created_at': user_message.created_at,
                    'selected_model': user_message.selected_model,
                },
                'ai_message': {
                    'id': ai_message.id,
                    'text': ai_message.text,
                    'ai': True,
                    'created_at': ai_message.created_at,
                    'selected_model': ai_message.selected_model,
                }
            }, encoder=DjangoJSONEncoder)
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid form data'}, status=400)

@require_POST
def clear_chat(request):
    """Clear all messages for the current session"""
    session_id = get_session_id(request)
    Message.objects.filter(session_id=session_id).delete()
    return JsonResponse({'status': 'success'})

@require_POST
def save_api_key(request):
    """Save the OpenAI API key"""
    session_id = get_session_id(request)
    form = ApiKeyForm(request.POST)
    
    if form.is_valid():
        api_key = form.cleaned_data['api_key']
        
        # Validate the API key
        if check_api_key(api_key):
            # Save or update the API key
            ApiKey.objects.update_or_create(
                session_id=session_id,
                defaults={'api_key': api_key}
            )
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'error': 'Invalid API key'}, status=400)
    
    return JsonResponse({'error': 'Invalid form data'}, status=400)

@require_POST
def remove_api_key(request):
    """Remove the OpenAI API key"""
    session_id = get_session_id(request)
    ApiKey.objects.filter(session_id=session_id).delete()
    return JsonResponse({'status': 'success'})

@csrf_exempt
@require_POST
def check_api_key_view(request):
    """Check if the API key is valid"""
    data = json.loads(request.body)
    api_key = data.get('api_key')
    
    if check_api_key(api_key):
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'error': 'Invalid API key'}, status=400)

@require_POST
def toggle_theme(request):
    """Toggle between light and dark theme"""
    current_theme = request.session.get('theme', 'dark')
    new_theme = 'light' if current_theme == 'dark' else 'dark'
    request.session['theme'] = new_theme
    return JsonResponse({'theme': new_theme})

