from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    _id = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()

class TeamSerializer(serializers.Serializer):
    _id = serializers.CharField()
    name = serializers.CharField()
    members = serializers.ListField()

class ActivitySerializer(serializers.Serializer):
    _id = serializers.CharField()
    user_id = serializers.CharField()
    activity_type = serializers.CharField()
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    _id = serializers.CharField()
    user_id = serializers.CharField()
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    _id = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
