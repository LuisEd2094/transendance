from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
import json
from .models import Conversation, Message


@csrf_exempt
def create_conversation(request):
    data = json.loads(request.body)
    participant_ids = data.get('participant_ids', [])
    participants = User.objects.filter(id__in=participant_ids)
    if not participants:
        return JsonResponse({'error': 'No valid participants found'}, status=400)
    
    conversation = Conversation.objects.create()
    conversation.participants.set(participants)
    return JsonResponse({
        'id': conversation.id,
        'participant_ids': list(participants.values_list('id', flat=True)),
        'created_at': conversation.created_at.isoformat()
    })

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        conversation = get_object_or_404(Conversation, id=data['conversation_id'])
        sender = request.user
        message = Message.objects.create(
            conversation=conversation,
            sender=sender,
            content=data['content']
        )
        return JsonResponse({'id': message.id, 'content': message.content, 'sender': sender.username, 'created_at': message.created_at.isoformat()})
    return JsonResponse({'error': 'Invalid request method'}, status=400)
