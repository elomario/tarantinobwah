from django.db import models
from members.models import Member
from events.models import Event

# Create your models here.

class Ecomment(models.Model):
	member_commenting = models.ForeignKey(Member) 
	event_commenting_on = models.ForeignKey(Event)
	posting_date = models.DateTimeField('published on:', auto_now_add = True)
	core_of_comment = models.TextField()
	def __str__(self):
		return self.member_commenting