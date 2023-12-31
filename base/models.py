from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    fare = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)   
    description = models.TextField()
    

    def __str__(self):
        return self.name

