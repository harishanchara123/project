from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

class Advisor(models.Model):
    AdvisorId = models.AutoField(primary_key=True)
    AdvisorName = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default="")

    def __str__(self):
        return self.DepartmentId

class Book(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Departmet = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default="")
    DateOfJoining = models.DateField()

  