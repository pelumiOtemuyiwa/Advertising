from django.db import models

# Create your models here.
class Advertisingcampaign(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    createdate = models.CharField(max_length=225)
    totalbudget = models.CharField(max_length=225)
    dailybudget = models.CharField(max_length=225)
    image = models.ImageField(upload_to='images')
   
