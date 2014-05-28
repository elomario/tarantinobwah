from django.db import models

class Presentation(models.Model):
	title = models.CharField(max_length = 100)
	text = models.TextField();
	def __str__(self):
		return self.title

class Image(models.Model):
	presentation = models.ForeignKey(Presentation)
	image = models.ImageField(upload_to = 'static/images')

class Video(models.Model):
	presentation = models.ForeignKey(Presentation)
	video = models.CharField(max_length = 100)