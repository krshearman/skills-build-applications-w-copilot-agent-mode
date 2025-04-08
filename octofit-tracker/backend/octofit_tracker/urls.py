"""
URL configuration for octofit_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from .views import UsersView, TeamsView, ActivityView, LeaderboardView, WorkoutsView
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activity': '/api/activity/',
        'leaderboard': '/api/leaderboard/',
        'workouts': '/api/workouts/',
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('api/', api_root, name='api-root'),
    path("admin/", admin.site.urls),
    path('api/users/', UsersView.as_view(), name='users'),
    path('api/teams/', TeamsView.as_view(), name='teams'),
    path('api/activity/', ActivityView.as_view(), name='activity'),
    path('api/leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    path('api/workouts/', WorkoutsView.as_view(), name='workouts'),
]
