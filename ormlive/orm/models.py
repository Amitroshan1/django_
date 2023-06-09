from django.db import models

# Create your models here.
class teacher(models.Model):
    firstname=models.CharField( max_length=100) 
    surname = models.CharField(max_length=100)
    
    def __str__(self):
        return self.firstname
    
    
class student(models.Model):
    firstname = models.CharField( max_length=50)
    surname= models.CharField(max_length=100)
    age = models.IntegerField()
    classroom =models.IntegerField()
    
    def __str__(self):
        return self.firstname
