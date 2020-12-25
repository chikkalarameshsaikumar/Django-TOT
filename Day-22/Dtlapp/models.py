from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Upd(models.Model):
	g = [('M',"Male"),('F',"Female")]
	age = models.IntegerField(default=18)
	gender = models.CharField(max_length=7,choices=g)
	im = models.ImageField(upload_to="Profile_pics/",default="profile.jpeg")
	p = models.OneToOneField(User,on_delete=models.CASCADE)

@receiver(post_save,sender=User)
def CrtPfle(sender,instance,created,**kwargs):
	 if created:
	 	Upd.objects.create(p=instance)