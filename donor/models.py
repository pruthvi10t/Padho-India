from django.db import models

# Create your models here.
class donor(models.Model):
	name = models.CharField(max_length = 64)
	phone_number = models.IntegerField()
	#school_name = models.CharField(default="nit")
	def __str__(self):
		return f"{self.name}  {self.phone_number} {self.school_name}"