from django.db import models
from django.urls import reverse
from django.contrib.auth.models import Permission, User


# Create your models here.

class Register (models.Model):
    user_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100)


    def get_absolute_url(self):
        return reverse('signup', kwargs={'pk': self.pk})

    def __str__(self):
        return self.user_id
