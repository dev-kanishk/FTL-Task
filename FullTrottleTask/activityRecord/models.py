from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

class User(AbstractUser):
    id = models.CharField(primary_key=True ,max_length=9, validators=[MinLengthValidator(9)])
    real_name = models.CharField(max_length = 100)
    tz = models.CharField(max_length = 100, default="Asia/kolkata")

    def __str__(self):
        return self.real_name


class activity_period(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, related_name='activity_periods',  on_delete=models.CASCADE)

    def __str__(self):
        to_display = str(self.start_time) + " to " + str(self.end_time)
        return to_display


