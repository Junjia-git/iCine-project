from django.db import models
from django.template.defaultfilters import slugify
from custom_user.models import UserProfile


class ClassifyModel(models.Model):
    name = models.CharField(max_length=512, verbose_name = "Genres")
    class Meta:
        verbose_name = "Movie Type"
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ClassifyModel, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class MovieModel(models.Model):
    name = models.CharField(max_length=128, verbose_name = "Title")
    detail = models.TextField(null=True, default="", verbose_name = "Content")
    pic = models.ImageField(upload_to = "image", verbose_name = "Images")
    actor = models.CharField(max_length = 512, verbose_name = "Actors")
    duration = models.IntegerField(verbose_name = "Duration")
    star = models.FloatField(verbose_name = "Rate")
    publish_time = models.DateTimeField(verbose_name = "Publ")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name = "Create time")
    classify = models.ForeignKey(ClassifyModel, related_name="classify", verbose_name = "Classify", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = verbose_name


# Comment forms
class CommentModel(models.Model):
    '''
    Multiple comment available
    '''
    person = models.ForeignKey(UserProfile, unique=False, verbose_name="Comment User",on_delete=models.CASCADE)
    content = models.TextField(null=True, default="", verbose_name = "Comment context")
    score = models.FloatField(verbose_name = "Score", default=4)
    # Comment Time
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Comment Time")
    movie = models.ForeignKey(MovieModel, related_name="tie_comment", verbose_name = "Comment page", on_delete=models.CASCADE)
    class Meta:
        ordering = ['-create_time']

class FavorateModel(models.Model):
    person = models.ForeignKey(UserProfile, unique=False, verbose_name="Colectioner", on_delete=models.CASCADE)
    movie = models.ForeignKey(MovieModel, verbose_name="movie", on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Colection time")

    class Meta:
        ordering = ['-create_time']