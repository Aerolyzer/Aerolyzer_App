from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Image(models.Model):
	imageId = models.AutoField(primary_key=True)
	filename = models.FileField(upload_to='../../../installDir/aerolyzerImgs', default = "none")
	exif = models.CharField(max_length=200)
	misr = models.CharField(max_length=200)
	wunder = models.CharField(max_length=200)
	results = models.CharField(max_length=200)

	def __unicode__(self):
		return self.results

class Gallery(models.Model):
	imageId = models.ForeignKey(Image)
	username = models.CharField(max_length=30)

	def __unicode__(self):
		return self.username
