from django.db import models

# Create your models here.
class Landing_Page(models.Model):
	title = models.CharField(max_length=200)
	blurb = models.CharField(max_length=200)
	headshot = models.ImageField()
	social_media_icon = models.ImageField(blank=True, null=True)
	social_media_icon_url = models.URLField(blank=True, null=True)


class Contact_Me(models.Model):
	name = models.CharField(max_length=200)
	email_address = models.EmailField()
	website_type = models.CharField(max_length=140)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
