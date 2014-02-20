from django.db import models

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=30)
    account = models.CharField(max_length=50)
    state_of_account= models.CharField(max_length=60)
  
