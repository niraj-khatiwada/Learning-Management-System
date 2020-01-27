from django.db import models

from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager

from .validators import validate_username

from django.utils.timezone import now
# Create your models here

class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Email must be provided')
        if not username:
            raise ValueError('Username must be provided')
        user = self.model(
        email = self.normalize_email(email),
        username = username
        )  
        user.set_password(password)
        user.save(using= self._db)
        return user


    def create_staffuser(self, email, username, password):
        user = self.create_user(
            email =email,
            username = username,
            password = password.password,

        )
        user.is_staff = True
        user.save(using = self._db  )
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = email,
            username = username,
            password = password,
           
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using = self._db)
        return user

class Account(AbstractBaseUser):
    email           =models.EmailField(max_length=255, unique=True, verbose_name='Email')
    username =      models.CharField(max_length=255, unique=True, help_text='Username can have "Numbers A-Z a-z _ - ." only', validators=[validate_username])
    is_manager =    models.BooleanField(default=False)
    is_teacher =    models.BooleanField(default=False)
    is_student =    models.BooleanField(default=False)
    is_suspended =  models.BooleanField(default=False)
    is_active =     models.BooleanField(default=True)
    is_staff =      models.BooleanField(default=False)
    is_admin =      models.BooleanField(default=False)
    date_joined     = models.DateTimeField(verbose_name='Date Joined',auto_now_add= True)
    last_login      = models.DateTimeField(verbose_name='Last Active', auto_now=True)
        
    class Meta:
        db_table = 'Account'

    def __str__(self):
        return self.email
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()

    def has_perm(self, perm, object=None):
        return True

    def has_module_perms(self, app_label):
        return True
