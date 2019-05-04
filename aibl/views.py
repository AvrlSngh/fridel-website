from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from webpush import send_user_notification
import json
from django.http.response import JsonResponse, HttpResponse

@require_POST
@csrf_exempt
def send_push(request):
    try:
        body = request.body
        data = json.loads(body)

        if 'head' not in data or 'body' not in data or 'id' not in data:
            return JsonResponse(status=400, data={"message": "Invalid data format"})

        user_id = data['id']
        user = get_object_or_404(User, pk=user_id)
        payload = {'head': data['head'], 'body': data['body']}
        send_user_notification(user=user, payload=payload, ttl=1000)
        print("sent..")

        return JsonResponse(status=200, data={"message": "Web push successful"})
    except TypeError:
        return JsonResponse(status=500, data={"message": "An error occurred"})

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def terms(request):
    return render(request, 't&c.html')

def manifest(request):
    return render(request, 'main.js')
