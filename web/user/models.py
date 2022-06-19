from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    phone_number = models.CharField(max_length=20, unique=True, blank=False)
    otp = models.CharField(max_length=6, blank=False)
    user_attempt = models.IntegerField(default=0)
    created_ts = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_ts = models.DateTimeField(auto_now=True, null=True, blank=True)


class AddEmails(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user_emails")
    email = models.EmailField(blank=False)
