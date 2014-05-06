from django.db import models
from teams.models import Team

# Create your models here.
class Member(models.Model):
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 254,unique = True)
	phone_number = models.CharField(max_length = 13)
	teams = models.ManyToManyField(Team)
	def __unicode__(self):  
        	return self.email
