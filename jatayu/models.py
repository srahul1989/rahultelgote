from django.db import models

# Create your models here.
class UserInfo(models.Model):
	userid = models.CharField(max_length=150)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	emailid = models.CharField(max_length=150)
	mobile_number = models.IntegerField(default=9876543210)
	password = models.CharField(max_length=500)
		