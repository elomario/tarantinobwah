from django.db import models
from members.models import Member, Team

class Project(models.Model):
	title = models.CharField(max_length = 200)
	description = models.TextField()
	team = models.ForeignKey(Team)
	members = models.ManyToManyField(Member)
	deadline = models.DateField()
	def __str__(self):  
        	return self.title