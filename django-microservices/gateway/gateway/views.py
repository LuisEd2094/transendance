import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        print("I am here")
        data = json.loads(request.body)
        response = requests.post("http://userservice:8000/user/create/", json=data)
        return JsonResponse(response.json())
