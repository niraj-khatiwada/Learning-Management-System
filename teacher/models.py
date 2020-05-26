from django.db import models
from account.models import Account
# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20,default='98xxxxxxxx')
    deparment = models.CharField(null=True,blank=True,max_length=50)
    profile = models.ImageField(blank=True,null=True,upload_to='profile/')
    subject = models.BooleanField(max_length=200,blank=True,null=True)
    user = models.OneToOneField(Account,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

