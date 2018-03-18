from django.db import models

# Create your models here.

class RegisterLogin(models.Model):
	companyname = models.CharField(max_length=100)
	username = models.CharField(max_length=30)
	email = models.EmailField()
	password = models.CharField(max_length=50,null=True)
	activated = models.BooleanField(default=False)

	def __str__(self):
		return self.username

class UserOTP(models.Model):
	username = models.CharField(max_length=30)
	email = models.EmailField()
	otp = models.CharField(max_length=5)
	startTime = models.DateTimeField()
	endTime = models.DateTimeField()

	def __str__(self):
		return self.username