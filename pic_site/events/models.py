from django.db import models
from members.models import Member
from members.teams import Team

# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length = 200)
	date = models.DateTimeField('date')
	place = models.CharField(max_length = 200)
	participants = models.ManyToManyField(Member)
	description = models.TextField() 
        def __unicode__(self):
                return self.name
