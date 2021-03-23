from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import related

class User(AbstractUser):
    pass

class Tracking(models.Model):
    count = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f'{self.count}'

class Habit(models.Model):
    habit = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    goal = models.IntegerField()
    tracker = models.ForeignKey(Tracking, on_delete=models.CASCADE, related_name='tracker')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    
    def __str__(self):
        return self.habit


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')        

    def __str__(self):
        return f'{self.user}'