from django.contrib import admin
from accounts.models import UserProfile, Patient, Attendance

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Patient)
admin.site.register(Attendance)
