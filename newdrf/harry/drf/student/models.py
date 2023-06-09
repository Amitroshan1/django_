from django.db import models
import uuid
# Create your models here.



class basemodel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4())
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        abstract= True


class children(basemodel):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)


    def __str__(self):
        return self.name
