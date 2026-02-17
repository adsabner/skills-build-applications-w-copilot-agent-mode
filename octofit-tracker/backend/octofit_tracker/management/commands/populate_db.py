from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel Team')
        dc = Team.objects.create(name='DC', description='DC Team')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        tony = User.objects.create(name='Tony Stark', email='tony@stark.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@rogers.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@wayne.com', team=dc)
        diana = User.objects.create(name='Diana Prince', email='diana@prince.com', team=dc)

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        pushups = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        situps = Workout.objects.create(name='Situps', description='Core', difficulty='Medium')
        running = Workout.objects.create(name='Running', description='Cardio', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user=tony, workout=pushups, date=timezone.now(), duration=30, calories_burned=200)
        Activity.objects.create(user=steve, workout=situps, date=timezone.now(), duration=25, calories_burned=180)
        Activity.objects.create(user=bruce, workout=running, date=timezone.now(), duration=40, calories_burned=350)
        Activity.objects.create(user=diana, workout=pushups, date=timezone.now(), duration=35, calories_burned=220)

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(team=marvel, points=380)
        Leaderboard.objects.create(team=dc, points=570)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
