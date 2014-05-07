from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
	DEPARTMENT_CHOICES = (
	        ('BIM', 'BIM'),
	        ('BS', 'BS'),
	        ('GCU', 'GCU'),
	        ('GE', 'GE'),
	        ('GEN', 'GEN'),
	        ('GI', 'GI'),
		('GMC', 'GMC'),
                ('GMD', 'GMD'),
	        ('GMPP', 'GMPP'),
	        ('IF', 'IF'),
	        ('PC', 'PC'),
	        ('SGM', 'SGM'),
   		('TC', 'TC'),
	)
	YEAR_IN_SCHOOL_CHOICES = (
	        ('1', '1'),
	        ('2', '2'),
	        ('3', '3'),
	        ('4', '4'),
	        ('5', '5'),
	)
	user = models.OneToOneField(User)
	department = models.CharField(max_length = 4, choices = DEPARTMENT_CHOICES, blank = True)
	school_year = models.CharField(max_length = 1, choices = YEAR_IN_SCHOOL_CHOICES, blank = True)
	phone_number = models.CharField(max_length = 13, blank = True)
	teams = models.ManyToManyField('members.Team', null = True, blank = True)
	def __unicode__(self):  
        	return self.user.username

class Team(models.Model):
	team_name = models.CharField(max_length = 200)
	team_members = models.ManyToManyField('members.Member', blank = True, null = True)
	team_manager = models.ForeignKey('members.Member', related_name='+', blank = True, null = True)
	def __unicode__(self):  
        	return self.team_name
