from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    age = models.IntegerField(blank=True, null=True)
    university = models.CharField(max_length=20)
    image = models.ImageField(upload_to='assets_img/', blank=True)

    def __str__(self):
        return self.id_number




class Room(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    capacity = models.IntegerField()
    image = models.ImageField(upload_to='assets_img/', blank=True)
    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking from {self.user.username} to {self.room.name}"

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


