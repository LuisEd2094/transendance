from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
import json

User = get_user_model()

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.create_user(username=data["username"], password=data["password"])
        return JsonResponse({"id": user.id, "username": user.username})
