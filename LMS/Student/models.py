from django.db import models

from Account.models import Account

from .validators import validate_designation, validate_name

from Account.validators import validate_username

# Create your models here.

class Student(models.Model):
    name = models.CharField(verbose_name='Full Name', max_length=50, validators=[validate_name])
    username =      models.CharField(max_length=255, unique=True, help_text='Username can have "Numbers A-Z a-z _ - ." only', validators=[validate_username])
    designation = models.CharField(max_length=50, validators=[validate_designation])
    profile_iamge = models.ImageField(upload_to='media/Student', blank=True, null=True)
    description = models.TextField(blank=True, null= True)
    user = models.OneToOneField(Account, on_delete= models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Student'

    def save(self, force_insert= False, force_update= False):
        self.name = self.name.capitalize()
        self.designation = self.designation.capitalize()
        self.description = self.description.capitalize()
        super(Student, self).save(force_insert, force_update)