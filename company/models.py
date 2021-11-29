from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from users.models import *

# Create your models here.


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