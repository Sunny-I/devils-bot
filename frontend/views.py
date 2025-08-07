from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import requests

def home(request):
    """Render the main chat interface"""
    return render(request, 'home_page.html')

@csrf_exempt
def chat_api(request):
    """Handle chat API requests to AI model"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            
            if not user_message:
                return JsonResponse({'error': 'Message is required'}, status=400)
            
            # Call AI model API (using placeholder API key)
            ai_response = call_ai_model(user_message)
            
            return JsonResponse({
                'response': ai_response,
                'status': 'success'
            })
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def call_ai_model(message):
    """Call the Google Gemini API"""
    try:
        # Get API key from settings
        api_key = settings.GEMINI_API_KEY
        
        if not api_key:
            return "API key not configured. Please add your Gemini API key to the .env file."
        
        # Google Gemini API configuration
        api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"
        
        headers = {
            "Content-Type": "application/json"
        }
        
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": f"You are a friendly and reliable AI personal assistant. Speak in a warm, approachable tone while being clear, concise, and helpful. Your goal is to answer the user's questions thoughtfully, just like a smart and dependable human assistant would. User: {message}\n\nAssistant:"
                        }
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.7,
                "topK": 40,
                "topP": 0.95,
                "maxOutputTokens": 500,
                "stopSequences": []
            },
            "safetySettings": [
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                }
            ]
        }
        
        response = requests.post(api_url, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if 'candidates' in result and len(result['candidates']) > 0:
                if 'content' in result['candidates'][0] and 'parts' in result['candidates'][0]['content']:
                    return result['candidates'][0]['content']['parts'][0]['text']
                else:
                    return "Sorry, I couldn't generate a response. Please try again."
            else:
                return "Sorry, I couldn't generate a response. Please try again."
        else:
            return f"Sorry, I encountered an error. Please try again later. (Status: {response.status_code})"
            
    except requests.exceptions.RequestException as e:
        return "Sorry, I'm having trouble connecting to the AI service. Please try again later."
    except Exception as e:
        return "Sorry, something went wrong. Please try again."
