from django.db import models
# Create your models here.
class Presentation(models.Model):
	title = models.CharField(max_length = 100)
	text = models.TextField();
	#publication_date = models.DateTimeField('published on:', auto_now_add = True)
	def __str__(self):
		return self.title

class Image(models.Model):
	presentation = models.ForeignKey(Presentation)
	image = models.ImageField(upload_to='static/pic_site')

class Video(models.Model):
	presentation = models.ForeignKey(Presentation)
	video = models.CharField(max_length = 100)