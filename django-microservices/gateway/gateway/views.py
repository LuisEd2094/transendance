import requests
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging

logger = logging.getLogger(__name__)

def test_logging(request):
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
    return HttpResponse("Log messages generated.")

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        response = requests.post("http://userservice:8000/user/create/", json=data)
        try:
            response_data = response.json()
        except ValueError:
            return JsonResponse({"error": "Invalid response from userservice"}, status=500)
        return JsonResponse(response_data, status=response.status_code)

@csrf_exempt
def create_conversation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        response = requests.post("http://userservice:8000/chat/create_conversation/", json=data)
        try:
            response_data = response.json()
        except ValueError:
            return JsonResponse({"error": "Invalid response from chatservice"}, status=500)
        return JsonResponse(response_data, status=response.status_code)

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        data = json.loads(request.body)
        chat_service_url = "http://chatservice:8000/chat/send_message/"
        response = requests.post(chat_service_url, json=data)
        try:
            response_data = response.json()
        except ValueError:
            return JsonResponse({"error": "Invalid response from chatservice"}, status=500)
        return JsonResponse(response_data, status=response.status_code)