from django.db import models
from django.urls import reverse

# Create your models here.
class company(models.Model):
    name = models.CharField( max_length=50)
    ceo = models.CharField( max_length=50)
    origin = models.CharField( max_length=50)
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product:details", kwargs={"pk": self.pk})
    
    
class product(models.Model):
    p_name = models.CharField(max_length=50)
    cc = models.IntegerField()
    milage =  models.IntegerField()
    price = models.IntegerField()
    
    
    # connecting two models
    
    company= models.ForeignKey("company", related_name="company", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.p_name