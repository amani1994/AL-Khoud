from django.db import models

# Create your models here.
<<<<<<< HEAD

class Profile(models.Model):
=======
'''class Profile(models.Model):
     
>>>>>>> e8895b648912baae90c30842424d4455ad2574be
     #user = models.OneToOneField(User, on_delete=models.CASCADE)
     avatar = models.ImageField(upload_to="images/", default="images/default.jpg")
     level = models.IntegerField()
     age = models.IntegerField()
     city = models.CharField(max_length=200)'''
     
'''class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    decription = models.TextField()'''

class Club (models.Model):
    #category = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)
    type_choices = models.TextChoices("Club Type", ["Gym", "Self_defense ","Equestrian"])
    #city_choices = models.TextChoices("Club Type", ["Riyadh", "Jeddah ","Hail", 'Dammam'])
    name = models.CharField(max_length=200)
<<<<<<< HEAD
    type = models.CharField(max_length=200 , default=None) # نغيرها إلى تشويس
    decription = models.TextField()
    city = models.CharField(max_length=200)
    discrit = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    is_enrolled = models.BooleanField(default=False) # set to true if the club accept the subscriber.

'''class Offers (models.Model):
=======
    decription = models.TextField()
    #city = models.CharField(max_length=64,default='Jeddah', choices=type_choices.choices)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    type = models.CharField(max_length=64,default='Equestrian', choices=type_choices.choices)

'''
class Offers (models.Model):
>>>>>>> e8895b648912baae90c30842424d4455ad2574be
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    discount = models.IntegerField()
    description = models.TextField()

class Package (models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    details = models.TextField()
    duration = models.CharField(max_length=200)'''
    

'''class Subscriber(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=200)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)'''

class Coach (models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    social_account = models.CharField(max_length=200)
    experience = models.CharField(max_length=200) #عدد  سنوات الخبرة للمدرب
    phone_number = models.IntegerField()

'''class Tournament(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    tournament_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
'''


'''class Enroll(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    is_enrolled = models.BooleanField(default=False)'''


'''class Payment(models.Model):
    #club = models.ForeignKey(Club, on_delete=models.CASCADE)
    #subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=200)
    card_holder_name = models.CharField(max_length=400)
    expired_date = models.DateField()
    cvv = models.IntegerField()
    # is_paid = models.BooleanField(default=False)'''

'''class Review(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.FloatField()'''


class Contact (models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()'''