from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data using MongoDB commands
        client = MongoClient()
        db = client['octofit_db']
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', age=30, gender='Male'),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', age=35, gender='Male'),
            User(email='zerocool@mhigh.edu', name='Steve Rogers', age=32, gender='Male'),
            User(email='crashoverride@mhigh.edu', name='Natasha Romanoff', age=28, gender='Female'),
            User(email='sleeptoken@mhigh.edu', name='Bruce Banner', age=40, gender='Male'),
        ]
        for user in users:
            user.save()

        # Create teams with valid references to User objects
        blue_team = Team(name='Blue Team')
        blue_team.save()
        blue_team.members.add(users[0])
        blue_team.members.add(users[1])

        gold_team = Team(name='Gold Team')
        gold_team.save()
        gold_team.members.add(users[2])
        gold_team.members.add(users[3])
        gold_team.members.add(users[4])

        # Create activities with user ObjectId references
        activities = [
            Activity(user=users[0].id, activity_type='Cycling', duration=60, date='2025-04-08'),
            Activity(user=users[1].id, activity_type='Crossfit', duration=120, date='2025-04-07'),
            Activity(user=users[2].id, activity_type='Running', duration=90, date='2025-04-06'),
            Activity(user=users[3].id, activity_type='Strength', duration=30, date='2025-04-05'),
            Activity(user=users[4].id, activity_type='Swimming', duration=75, date='2025-04-04'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries with user ObjectId references
        leaderboard_entries = [
            Leaderboard(user=users[0].id, points=100, rank=1),
            Leaderboard(user=users[1].id, points=90, rank=2),
            Leaderboard(user=users[2].id, points=95, rank=3),
            Leaderboard(user=users[3].id, points=85, rank=4),
            Leaderboard(user=users[4].id, points=80, rank=5),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event', duration=60),
            Workout(name='Crossfit', description='Training for a crossfit competition', duration=120),
            Workout(name='Running Training', description='Training for a marathon', duration=90),
            Workout(name='Strength Training', description='Training for strength', duration=30),
            Workout(name='Swimming Training', description='Training for a swimming competition', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
