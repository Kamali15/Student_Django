from django.db import models

# Create your models here.
class Student(models.Model):
    studentid=models.CharField(max_length=10,primary_key=True)
    name=models.CharField(max_length=30)
    phone=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
    def __str__(self):
        return self.name
