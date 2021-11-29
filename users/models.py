from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from company.models import *

# Create your models here.


GENDER_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),

     
)

class Customer(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, unique=True)
    age = models.IntegerField()
    gender = models.CharField( choices=GENDER_CHOICES, max_length=50)
    mobile = models.CharField(max_length=12)
    country = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)





class CustomerHistory(models.model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE)
    deals = models.ForeignKey(Deal, on_delete=models.CASCADE)


