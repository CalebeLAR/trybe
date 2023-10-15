from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class WorkoutPlan(models.Model):
    client = models.OneToOneField(
        # related_name é pra pegar o workoutPlan atraves de Client
        Client, on_delete=models.CASCADE, related_name="workout_plan"
    )
    personal_trainer = models.ForeignKey(
        # related_name é pra pegar o workoutPlan atraves de User
        User, on_delete=models.CASCADE, related_name="workout_plan",
    )
    workout = models.TextField()

    def __str__(self):
        return f"{self.client.name} - Workout Plan"
