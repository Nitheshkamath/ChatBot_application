# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .chatbot_logic import extract_intent_and_entity, generate_response

# View to render the chatbot interface
def chatbot_view(request):
    return render(request, 'chatbot.html')

# View to process user input and return chatbot response
def get_response(request):
    if request.method == "POST":
        user_input = request.POST.get('message')
        intent, entity = extract_intent_and_entity(user_input)
        response = generate_response(intent, entity)
        return JsonResponse({'response': response})
    return JsonResponse({'response': 'Error: Invalid request.'})
