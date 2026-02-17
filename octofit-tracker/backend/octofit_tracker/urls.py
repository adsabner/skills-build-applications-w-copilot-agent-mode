
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from django.http import JsonResponse
import os
from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')

# Custom API root to show full URLs with $CODESPACE_NAME
def custom_api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME', '')
    base_url = f"https://{codespace_name}-8000.app.github.dev" if codespace_name else "http://localhost:8000"
    return JsonResponse({
        "activities": f"{base_url}/api/activities/",
        "users": f"{base_url}/api/users/",
        "teams": f"{base_url}/api/teams/",
        "leaderboard": f"{base_url}/api/leaderboard/",
        "workouts": f"{base_url}/api/workouts/",
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', custom_api_root, name='custom-api-root'),
    path('', views.api_root, name='api-root'),
]
