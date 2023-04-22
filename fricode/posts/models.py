from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Categories(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		ordering = ('name',)
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

#	def __str__(self):
#return self.post_title

class Comments(models.Model):
	comment = models.TextField()


class Post(models.Model):
	authar_name    = models.ForeignKey(User, max_length=100, on_delete=models.CASCADE)
	post_title     = models.CharField(max_length=250)
	key_word1      = models.CharField(max_length=100, null=True, blank=True)
	key_word2      = models.CharField(max_length=100, null=True, blank=True)
	key_word3      = models.CharField(max_length=100, null=True, blank=True)
	category       = models.ForeignKey(Categories, on_delete=models.CASCADE)
	image          = models.ImageField(upload_to='post_images', blank=True, null=True)
	image2         = models.ImageField(upload_to='post_images', blank=True, null=True)
	image3         = models.ImageField(upload_to='post_images', blank=True, null=True)
	body           = models.TextField()
	post_date      = models.DateField(auto_now_add=True)
	is_pulished    = models.BooleanField(default=True)
	comment        = models.ForeignKey(Comments, blank=True, null=True ,on_delete=models.CASCADE)



