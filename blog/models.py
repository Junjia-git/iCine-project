from django.db import models
from django.utils import timezone
from custom_user.models import UserProfile
from django.urls import reverse
from PIL import Image

class Post(models.Model):
	author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	subTitle = models.TextField(max_length=100, default='Welcome to see my new blog!')
	content = models.TextField()
	# img = models.ImageField(upload_to='image')
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	# def save(self):
	# 	super().save()

	# 	img = Image.open(self.image.path)

	# 	if img.height > 420 or img.width > 196.88:
	# 		output_size = (420,196.88)
	# 		img.thumbnail(output_size)
	# 		img.save(self.image.path)

	def get_absolute_url(self):
		return reverse('blog:postDetail', kwargs={'pk': self.pk})

