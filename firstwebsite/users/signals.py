from django.db.models.signals import post_save  #it gets the singnal  when a registration is done in views i.e form.save()
from django.contrib.auth.models import User # need to import user models
from django.dispatch import receiver  #reciever which recirvs signals
from .models import profile



@receiver(post_save,sender=User)
def build_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)



@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()