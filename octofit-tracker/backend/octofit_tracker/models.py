from djongo import models
from djongo.models import ArrayReferenceField

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    class Meta:
        db_table = 'users'

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = ArrayReferenceField(to=User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'teams'

class Activity(models.Model):
    user = models.ObjectIdField()
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'activity'

class Leaderboard(models.Model):
    user = models.ObjectIdField()
    points = models.IntegerField()
    rank = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    class Meta:
        db_table = 'workouts'
