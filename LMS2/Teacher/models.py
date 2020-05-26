from django.db import models

# Create your models here.
from django.db import models

from Account.models import Account

from .validators import validate_name, validate_designation

from Account.validators import validate_username

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(verbose_name='Full Name', max_length=50, validators=[validate_name])
    username = models.CharField(max_length=255, unique=True, help_text='Username can have "Numbers A-Z a-z _ - ." only', validators=[validate_username])
    designation = models.CharField(max_length=50, validators=[validate_designation])
    profile_iamge = models.ImageField(upload_to='media/Student', blank=True, null=True)
    description = models.TextField(blank=True, null= True)
    user = models.OneToOneField(Account, on_delete= models.CASCADE)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'Teacher'

    def save(self, force_insert= False, force_update= False):
        self.name = self.name.capitalize()
        self.designation = self.designation.capitalize()
        super(Teacher, self).save(force_insert, force_update)