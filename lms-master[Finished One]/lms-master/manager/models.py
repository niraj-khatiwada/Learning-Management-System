from django.db import models
from account.models import Account
# Create your models here.

class Manager(models.Model):
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15)
    designation = models.CharField(null=True,blank=True,max_length=100)
    image = models.ImageField(blank=True,null=True,upload_to='profile/')
    user = models.OneToOneField(Account,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name
