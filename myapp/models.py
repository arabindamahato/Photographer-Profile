from django.db import models

# Create your models here.

class Photographer(models.Model):
	top_carousel_heading = models.CharField(max_length=100)
	top_carousel_paragraph = models.CharField(max_length=500)
	upper_content_heading = models.CharField(max_length=500)
	profile_picture = models.ImageField(upload_to='profile_picture', blank=True)
	profile_heading = models.CharField(max_length=50)
	profile_intro = models.CharField(max_length=100)
	lower_content_heading = models.CharField(max_length=500)
	
	def __str__(self):
		return self.profile_intro



class Subscriber(models.Model):
	full_name = models.CharField(max_length=50)
	email = models.EmailField()

	def __str__(self):
		return self.email


class Gallary(models.Model):
	gallary_image = models.ImageField(upload_to='gallary_image', blank=True)
	


class Content(models.Model):
	first_para = models.CharField(max_length=9000)
	second_para = models.CharField(max_length=9000)
	third_para = models.CharField(max_length=9000)

	def __str__(self):
		return self.first_para

