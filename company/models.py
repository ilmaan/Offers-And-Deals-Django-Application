from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from users.models import *

# Create your models here.


class Company(models.Model):

    
    company_name = models.CharField(blank=True,max_length=100,null=True)
    company_logo = models.ImageField(blank=True,null=True)
    company_type = models.CharField(max_length=100,blank=True)
    total_categories = models.IntegerField(blank=True,null=True)
    total_deals = models.IntegerField(default=1,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return str(self.id)


class Deal(models.Model):
    deal_company = models.ForeignKey(Company,on_delete=models.CASCADE)
    deal_title = models.CharField(max_length=100,blank=True,null=True)
    deal_price = models.FloatField(default=0)
    validity_from = models.DateTimeField(blank=True,null=True)
    validity_till = models.DateTimeField(blank=True,null=True)
    deal_description = models.CharField(blank=True,max_length=500,null=True)