from django.db import models
from django.contrib.auth.models import User

class SavedFlight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    temperature = models.IntegerField()
    pic_path = models.CharField(max_length=100)
    depart_from = models.CharField(max_length=100)
    flight_date = models.CharField(max_length=100)
    flight_price = models.CharField(max_length=100)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.city_name} ({self.flight_date})"
