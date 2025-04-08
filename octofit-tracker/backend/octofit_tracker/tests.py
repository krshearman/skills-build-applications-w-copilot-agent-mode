from django.test import TestCase
from .mongo_utils import MongoDBClient

class MongoDBTestCase(TestCase):
    def setUp(self):
        self.mongo_client = MongoDBClient()

    def tearDown(self):
        self.mongo_client.close()

    def test_users_collection(self):
        users = self.mongo_client.get_collection("users").find()
        self.assertIsNotNone(users)

    def test_teams_collection(self):
        teams = self.mongo_client.get_collection("teams").find()
        self.assertIsNotNone(teams)

    def test_activity_collection(self):
        activities = self.mongo_client.get_collection("activity").find()
        self.assertIsNotNone(activities)

    def test_leaderboard_collection(self):
        leaderboard = self.mongo_client.get_collection("leaderboard").find()
        self.assertIsNotNone(leaderboard)

    def test_workouts_collection(self):
        workouts = self.mongo_client.get_collection("workouts").find()
        self.assertIsNotNone(workouts)
