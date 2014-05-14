from django.db import models
from members.models import Member, Team

# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length = 200)
	date = models.DateTimeField('date')
	place = models.CharField(max_length = 200)
	participants = models.ManyToManyField(Member)
	description = models.TextField() 
	def __str__(self):
		return self.name
