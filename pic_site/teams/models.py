from django.db import models

# Create your models here.
class Team(models.Model):
	team_name = models.CharField(max_length = 200)
	team_members = models.ManyToManyField('members.Member', blank = True, null = True)
	#team_manager = models.ForeignKey('members.Member', related_name='+', blank = True, null = True)
	def __unicode__(self):  
        	return self.team_name
