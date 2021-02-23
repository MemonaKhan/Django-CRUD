from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    # here I forgot and used : instead of =, must remember this

