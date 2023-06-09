from django.db import models

# Create your models here.
class company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField( max_length=50,choices=(('IT','IT'),
                                                    ('non-it','non-it'),
                                                    ('mobile phones','mobile phones')))
    
    added_date = models.DateTimeField(auto_now=True)
    active= models.BooleanField(default=True)