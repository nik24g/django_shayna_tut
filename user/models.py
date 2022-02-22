from django.db import models
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.TextField()
    image = models.ImageField(upload_to="user/profile")
    phone = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = CustomUserManager()

    def __str__(self):
        return self.email
    

class Contact(models.Model):
    name = models.CharField(max_length=50)
    # char field always require max_length argument
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()

    def __str__(self):
        return self.email

class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    branch = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to="user/student")

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=30)
    employee_id = models.CharField(max_length=10)
    address = models.TextField()
    salary = models.IntegerField()

    def __str__(self):
        return self.name
    