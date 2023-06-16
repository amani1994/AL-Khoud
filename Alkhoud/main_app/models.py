from django.db import models

# Create your models here.
class Profile(models.Model):
     
     #user = models.OneToOneField(User, on_delete=models.CASCADE)
     avatar = models.ImageField(upload_to="images/", default="images/default.jpg")
     level = models.IntegerField()
     age = models.IntegerField()
     city = models.CharField(max_length=200)
     
'''class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    decription = models.TextField()'''

class Club (models.Model):
    #category = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200 , default=None)
    decription = models.TextField()
    city = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

class Offers (models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    discount = models.IntegerField()

class Package (models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    details = models.TextField()
    duration = models.CharField(max_length=200)

class Subscriber(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=200)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class Coach (models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    social_account = models.CharField(max_length=200)
    experience = models.CharField(max_length=200) #عدد  سنوات الخبرة للمدرب

class Tournament(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    tournament_name = models.CharField(max_length=200)
    date = models.DateTimeField()

class Enroll(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    is_enrolled = models.BooleanField(default=False)

class Payment(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=200)
    card_holder_name = models.CharField(max_length=400)
    expired_date = models.DateField()
    cvv = models.IntegerField()
    is_paid = models.BooleanField(default=False)

class Review(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.FloatField()


class Contact (models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()