from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
     
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="images/", default="images/default.jpg")
    about = models.CharField(max_length=2048, blank=True)
    level_choices = models.TextChoices("fitness level", ["Beginner", "Intermediate ","Advanced"])
    level = models.CharField(max_length=128, choices=level_choices.choices)
    age = models.IntegerField()
    city = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10, blank=True)
    instagram_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
