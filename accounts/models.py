from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=50, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class Patient(models.Model):
    name = models.CharField(max_length=100, default='Patient Name')
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=100, default='Male')

    def __str__(self):
        return self.name


class Attendance(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="Attendance_Patient")
    date = models.DateTimeField()
    present_status = models.BooleanField(default=False)

    def __str__(self):
        return self.patient.name
