from django.db import models

# Create your models here.
class moviedata(models.Model):
    name = models.CharField(max_length=100)
    duration = models.FloatField()
    rating = models.FloatField()
    typ = models.CharField(max_length=50,default='action')
    img = models.ImageField( upload_to="images/",default="images/none/noimg.jpg")
    
    def __str__(self):
        return self.name
    