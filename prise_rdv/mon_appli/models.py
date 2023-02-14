from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Coach(models.Model):
    name = models.CharField(max_length=100)
    coach_id = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.name
    
class Meta:
    app_label = 'mon_appli'
        
class Appointment(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.DurationField(default=30)
    session_object = models.TextField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.client} with {self.coach} on {self.date} at {self.start_time}"
    
    class Meta:
        app_label = 'mon_appli'
        
