from django.db import models

# Create your models here.

class MobileAlbum(models.Model):
	MobileUploadsDir = models.CharField(max_length=100)

	def __str__(self):
		return self.MobileUploadsDir

class DirectAlbum(models.Model):
	DirectUploadsDir = models.CharField(max_length=100)

	def __str__(self):
		return self.DirectUploadsDir

class Mobilepics(models.Model):
	MobileUploadsPics = models.CharField(max_length=100)
	directoryLink = models.ForeignKey(MobileAlbum, on_delete=models.CASCADE)

	def __str__(self):
		return self.MobileUploadsPics

class DirectUpload(models.Model):
	DirectUploadPics = models.CharField(max_length=100)
	directoryLink = models.ForeignKey(DirectAlbum, on_delete=models.CASCADE)

	def __str__(self):
		return self.DirectUploadPics

