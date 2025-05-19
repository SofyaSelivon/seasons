from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
import json
import logging
from .models import Season, MainVote
from django.views.decorators.csrf import csrf_protect
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.admin.views.decorators import staff_member_required

logger = logging.getLogger(__name__)

@ensure_csrf_cookie
def index(request):
    return render(request, 'index.html')
def season_view(request, season_name):
    season = get_object_or_404(Season, name__iexact=season_name)
    print(f"Season ID: {season.id}")
    return render(request, f'seasons/{season_name}.html', {
        'season': season
    })
@csrf_protect
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']
            first_name = data.get('first-name', '')
            last_name = data.get('last-name', '')
            logger.info(f"Попытка регистрации пользователя: {email}")
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            logger.info(f"Пользователь {email} успешно зарегистрирован.")

            return JsonResponse({
                "status": "success",
                "user": {
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name
                }
            })
        except Exception as e:
            logger.error(f"Ошибка регистрации: {str(e)}")
            return JsonResponse({"error": str(e)}, status=400)

def check_auth(request):
    if request.user.is_authenticated:
        return JsonResponse({
            "authenticated": True,
            "user": {
                "email": request.user.email,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name
            }
        })
    return JsonResponse({"authenticated": False})

@csrf_protect
def logout_user(request):
    logout(request)
    return JsonResponse({"message": "Вы успешно вышли"})

@csrf_protect
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({
                    "status": "success",
                    "user": {
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name
                    }
                })
            else:
                return JsonResponse({"error": "Неверный email или пароль!"}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@staff_member_required
def mainvote_counts(request):
    votes = MainVote.objects.all()
    data = [
        {"id": vote.id, "likes": vote.likes_count, "dislikes": vote.dislikes_count}
        for vote in votes
    ]
    return JsonResponse(data, safe=False)
