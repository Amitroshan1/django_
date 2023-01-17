from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    def __str__(self):    # to  see with item name 
        return self.item_name
    

    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200,default=" ")
    item_desc = models.CharField(max_length=200,default=" ")
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=600,default='https://p.kindpng.com/picc/s/79-798754_hoteles-y-centros-vacacionales-dish-placeholder-hd-png.png')
    
    
    def get_absolute_url(self):
        return reverse("foodapp:detail", kwargs={"pk": self.pk})
    