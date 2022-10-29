from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length = 122);
	phn = models.CharField(max_length = 12)
	email = models.CharField(max_length = 50);
	data = models.DateField();

	def __str__(self):
		return self.name


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE);
	bio = models.CharField(max_length = 100);

	def __str__(self):
		return str(self.user);