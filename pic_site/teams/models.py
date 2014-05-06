from django.db import models
#from members.models import Member

# Create your models here.
class Team(models.Model):
	team_name = models.CharField(max_length = 200)
	team_members = models.ManyToManyField('members.Member')
	team_manager = models.ForeignKey('members.Member',related_name='+')
	def __unicode__(self):  
        	return self.name
