from datetime import datetime
from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser,PermissionsMixin,AbstractBaseUser
# from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser,PermissionsMixin):
  
  email = models.EmailField(('email address'), unique=True)
  image = models.ImageField(default='default.jpg', upload_to='profile_pics')
  role = models.CharField(null=False,choices=([('doctor','doctor'),('patient','patient')]) ,max_length=10)
  firstname = models.CharField(max_length=100,null=False,default="")
  lastname = models.CharField(max_length=100,null=False,default="")
  username = models.CharField(max_length=20,null=False,default="")
  address = models.TextField(null=False,default="")
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)
  is_joined = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = CustomUserManager()

  def __str__(self):
    return self.email


class Blog(models.Model):
  id = models.AutoField(primary_key=True,null=False)
  title = models.TextField(max_length=100,null=False)
  content = models.TextField(max_length=10000,null=False)
  author_email = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
  author = models.CharField(max_length=100,null=True)
  date = models.DateTimeField(default=datetime)

  def __str__(self):
    return self.id

  class Meta:
    ordering=['id']
