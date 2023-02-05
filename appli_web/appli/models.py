from django.db import models

# Create your models here.

class Coach(models.Model):
    name = models.CharField(max_length=100)
    coach_id = models.CharField(max_length=50, unique=True)
    phone_numer = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.DurationField(default=30)
    session_object = models.TextField()

    def __str__(self):
        return f"{self.client} with {self.coach} on {self.date} at {self.start_time}"

