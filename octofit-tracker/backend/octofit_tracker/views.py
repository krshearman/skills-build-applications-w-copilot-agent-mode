from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .mongo_utils import MongoDBClient
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UsersView(APIView):
    def get(self, request):
        mongo_client = MongoDBClient()
        users = list(mongo_client.get_collection("users").find())
        mongo_client.close()
        return Response(UserSerializer(users, many=True).data)

class TeamsView(APIView):
    def get(self, request):
        mongo_client = MongoDBClient()
        teams = list(mongo_client.get_collection("teams").find())
        mongo_client.close()
        return Response(TeamSerializer(teams, many=True).data)

class ActivityView(APIView):
    def get(self, request):
        mongo_client = MongoDBClient()
        activities = list(mongo_client.get_collection("activity").find())
        mongo_client.close()
        return Response(ActivitySerializer(activities, many=True).data)

class LeaderboardView(APIView):
    def get(self, request):
        mongo_client = MongoDBClient()
        leaderboard = list(mongo_client.get_collection("leaderboard").find())
        mongo_client.close()
        return Response(LeaderboardSerializer(leaderboard, many=True).data)

class WorkoutsView(APIView):
    def get(self, request):
        mongo_client = MongoDBClient()
        workouts = list(mongo_client.get_collection("workouts").find())
        mongo_client.close()
        return Response(WorkoutSerializer(workouts, many=True).data)

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev/'
    return Response({
        'users': base_url + 'api/users/?format=api',
        'teams': base_url + 'api/teams/?format=api',
        'activities': base_url + 'api/activities/?format=api',
        'leaderboard': base_url + 'api/leaderboard/?format=api',
        'workouts': base_url + 'api/workouts/?format=api'
    })
