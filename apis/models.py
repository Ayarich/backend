from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.



#FOR EARN GIG BOARD OF DIRECTORS
class News(models.Model):
	title = models.CharField(max_length=200, null=True)
	description = models.TextField(max_length=200, null=True)
	image= models.ImageField(null=True,blank=True,upload_to="blogs")
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	image = CloudinaryField(default="blogs",null=True)
	def __str__(self):
		return self.title
	@property
	def imageURL(self):
		try:
			url=self.image.url
		except:
			url=''
		return url