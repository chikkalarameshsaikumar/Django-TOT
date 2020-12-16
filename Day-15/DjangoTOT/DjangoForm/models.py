from django.db import models

# Create your models here.


class Register(models.Model):
	gender_choices = [('Male',"Male"),('FeMale',"FeMale")]
	name = models.CharField(max_length=200,null=True)
	mobile_no = models.CharField(max_length=10,null=True)
	age = models.IntegerField()
	gender = models.CharField(max_length =10,choices=gender_choices,null=True)

