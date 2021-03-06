from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UsertInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    Profile = models.CharField(max_length=10)

    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        return self.user.username
