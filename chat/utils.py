import openai
import markdown
import re
from profanity_filter import ProfanityFilter

pf = ProfanityFilter()

def check_api_key(api_key):
    """Validate the OpenAI API key"""
    try:
        openai.api_key = api_key
        models = openai.Model.list()
        return True
    except Exception as e:
        print(f"API key validation error: {e}")
        return False

def clean_prompt(text):
    """Clean the prompt text by removing profanities"""
    return pf.censor(text)

def generate_chatgpt_response(prompt, api_key, gpt_version):
    """Generate a response from ChatGPT"""
    try:
        openai.api_key = api_key
        
        response = openai.ChatCompletion.create(
            model=gpt_version,
            messages=[
                {"role": "system", "content": "The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context and always responds in markdown format. If the AI does not know the answer to a question, it truthfully says it does not know."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print(f"ChatGPT API error: {e}")
        return f"Error: {str(e)}"

def generate_dalle_image(prompt, api_key):
    """Generate an image using DALL-E"""
    try:
        openai.api_key = api_key
        
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        
        return response['data'][0]['url']
    except Exception as e:
        print(f"DALL-E API error: {e}")
        return f"Error: {str(e)}"

def format_markdown(text):
    """Convert markdown to HTML"""
    # Process code blocks with syntax highlighting
    code_pattern = r'```(\w+)?\n(.*?)\n```'
    
    def replace_code_block(match):
        language = match.group(1) or ''
        code = match.group(2)
        return f'<pre><code class="language-{language}">{code}</code></pre>'
    
    text = re.sub(code_pattern, replace_code_block, text, flags=re.DOTALL)
    
    # Convert the rest of the markdown to HTML
    html = markdown.markdown(text)
    return html

