from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')
        self.user1 = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel.name)
        self.user2 = User.objects.create(name='Batman', email='batman@dc.com', team=dc.name)
        Activity.objects.create(user=self.user1, type='Running', duration=30, date='2026-01-01')
        Leaderboard.objects.create(team=marvel, points=100)
        Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout', suggested_for='Marvel')

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 2)

    def test_team_creation(self):
        self.assertEqual(Team.objects.count(), 2)

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_leaderboard_creation(self):
        self.assertEqual(Leaderboard.objects.count(), 1)

    def test_workout_creation(self):
        self.assertEqual(Workout.objects.count(), 1)
