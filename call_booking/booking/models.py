from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=20)
    email= models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    paid = models.BooleanField(default=False)
    hours = models.IntegerField(default=1)

    