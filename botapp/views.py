import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mebot import respone

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message')
            if not user_message:
                return JsonResponse({'error': 'No message provided'}, status=400)
            
            # Call your chatbot response logic
            bot_response = f"You said: {respone(str(user_message))}"
            return JsonResponse({'response': bot_response})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return HttpResponse(status=405)


def index(request):
    return render(request, 'index.html')
