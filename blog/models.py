from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify


# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre


class Article(models.Model):
    title = models.CharField(
        max_length=100
    )
    slug = models.SlugField(max_length=250, null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    body = models.TextField()
    photo = models.ImageField(
        upload_to='blogs/image',
        null=True
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    is_reviewed = models.BooleanField(
        default=False
    )
    claps = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.slug)])

    @property
    def get_claps(self):
        return self.claps


class ArticleReview(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    )
    reviewer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    comment = models.TextField()
