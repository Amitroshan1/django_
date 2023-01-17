from django.db import models

# Create your models here.

class emp_data(models.Model):
    emp_id = models.CharField(max_length=50)
    check_in_time = models.DateTimeField( auto_now=False, auto_now_add=False)
    check_out_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.emp_id
