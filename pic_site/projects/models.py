from django.db import models
from members.models import Member, Team

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length = 200)
	description = models.TextField()
	team = models.ForeignKey(Team)
	members = models.ManyToManyField(Member)
	deadline = models.DateField()
	def __unicode__(self):  
        	return self.title
