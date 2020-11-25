from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=23)
    lastname = models.CharField(max_length=23)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=32)
    Confirmpassword = models.CharField(max_length=32)
    createdat = models.DateTimeField(auto_now_add= True)
    updatedat = models.DateTimeField(auto_now_add=True)
