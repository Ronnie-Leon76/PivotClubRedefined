from django.contrib import messages
from django.contrib.auth import get_user_model
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from newsletter.models import Newsletter

User = get_user_model()


@csrf_exempt
def subscribe_newsletter(request):
    data: dict = {}

    email = request.POST.get('email')

    user = User.objects.filter(email=email).exists()
    subscribed_user = Newsletter.objects.filter(email=email).exists()

    if any([user, subscribed_user]):
        data['message'] = 'this email already exists'
        return JsonResponse(data)

    new_user = Newsletter(
        email=email
    )
    new_user.save()

    data['message'] = 'subscribed to our newsletter successfully'
    return JsonResponse(data)
