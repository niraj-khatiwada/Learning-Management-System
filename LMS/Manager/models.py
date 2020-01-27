from django.db import models

from Account.models import Account

# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=100, validators=[validate_name])
    designation = models.CharField(max_length=50, validators=[validate_deisgnation])
    profile_image = models.ImageField(upload_to='/media/manager', null= True, blank= True)
    description = models.TextField(blank=True, null=True)
    user = models.OneToOneField(Account, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Manager'

    
    def save(self, force_insert = False, force_update= False):
        self.name = self.name.capitalize()
        self.designation = self.designation.capitalize()
        self.description = self.description.capitalize()
        return super(Manager, self).save(force_insert, force_update)