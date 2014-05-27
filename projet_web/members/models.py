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
	def __str__(self):  
        	return self.user.username

class Team(models.Model):
	team_name = models.CharField(max_length = 200, unique = True)
	#To display all the members of a team, we should add a function that goes through the members table
	#And filter it, keeping only those who are part of the team
	team_manager = models.ForeignKey('members.Member', related_name='+', blank = True, null = True)
	def __str__(self):  
        	return self.team_name
