from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(name='Tony Stark', email='tony@stark.com', team=team)
        self.assertEqual(user.name, 'Tony Stark')
        self.assertEqual(user.team.name, 'Marvel')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='DC', description='DC Team')
        self.assertEqual(team.name, 'DC')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        self.assertEqual(workout.name, 'Pushups')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(name='Peter Parker', email='peter@parker.com', team=team)
        workout = Workout.objects.create(name='Situps', description='Core', difficulty='Medium')
        activity = Activity.objects.create(user=user, workout=workout, date='2024-01-01T10:00:00Z', duration=30, calories_burned=200)
        self.assertEqual(activity.user.name, 'Peter Parker')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.team.name, 'Marvel')
        self.assertEqual(leaderboard.points, 100)
