from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
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

class PDFUpload(models.Model):
	title = models.CharField(max_length = 100);
	pdf = models.FileField(upload_to = "pdf/", validators = [FileExtensionValidator(["pdf"])]);

	def __str__(self):
		return self.title;