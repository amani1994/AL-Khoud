from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):

    def __str__(self) -> str:
        return self.user.username

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profileimages', blank=True, default='default_image.jpg/' )
    phonenumber = models.CharField(max_length=10,blank=False,default="0502256188")