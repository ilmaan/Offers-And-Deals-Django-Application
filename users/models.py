from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
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



class Company(models.Model):
    
    company_name = models.CharField(max_length=100)
    company_logo = models.ImageField(blank=True)
    company_type = models.CharField()
    total_categories = models.IntegerField()
    total_deals = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)


class Deal(models.Model):
    deal_company = models.ForeignKey(Company,on_delete=models.CASCADE)
    deal_title = models.CharField(max_length=100)
    deal_price = models.FloatField(default=0)
    validity_from = models.DateTimeField()
    validity_till = models.DateTimeField()
    deal_description = models.CharField(max_length=500)


class CustomerHistory(models.model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE)
    deals = models.ForeignKey(Deal, on_delete=models.CASCADE)
    

