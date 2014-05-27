from django.db import models
from projects.models import Project
from members.models import Member

class Comment(models.Model):
	member_commenting = models.ForeignKey(Member) 
	project_commenting_on = models.ForeignKey(Project)
	posting_date = models.DateTimeField('published on:', auto_now_add = True)
	core_of_comment = models.TextField()