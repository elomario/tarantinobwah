from django.db import models
from projects.models import Project
from members.models import Member

# Create your models here.
class Comment(models.Model):
	member_commenting = models.ForeignKey(Member) 
	project_commenting_on = models.ForeignKey(Project)
	posting_date = models.DateTimeField('published on:', auto_now_add = True)
	core_of_comment = models.TextField()
	response_to = models.ForeignKey('comments.Comment',null = True, default = None)
