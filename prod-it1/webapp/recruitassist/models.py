# Author: Mohammad Marwan Qaiser
# Last Modified Date: 15/9/2019

# The following code is used to define the database schema


from django.db import models

class Providers(models.Model):
    ID = models.IntegerField(primary_key=True)
    LOCATION_NAME=models.CharField(max_length=30)
    SITE_NAME= models.CharField(max_length=255)
    CONTACT=models.CharField(max_length=20)
    ADDRESS=models.CharField(max_length=255)
    SITE_SUBURB=models.CharField(max_length=100)
    STATE=models.CharField(max_length=3)
    POSTCODE = models.IntegerField(null=True)
    URL=models.CharField(max_length=255, null=True)
    EMAIL_ADDRESS= models.EmailField(max_length=100)
    LATITUDE=models.FloatField(max_length=100, null=True)
    LONGITUDE=models.FileField(max_length=100, null=True)


