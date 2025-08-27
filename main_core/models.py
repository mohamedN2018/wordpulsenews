from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class NewsCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "News Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class NewsArticle(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to="articles/")
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, related_name="articles")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    is_breaking = models.BooleanField(default=False)  # <- هذا الحقل

    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.article}"


class Advertisement(models.Model):
    POSITIONS = [
        ("header", "Header"),
        ("sidebar", "Sidebar"),
        ("footer", "Footer"),
    ]

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="ads/")
    link = models.URLField()
    position = models.CharField(max_length=20, choices=POSITIONS)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.position})"



class FlickrPhoto(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='flickr_photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Flickr Photo"
        verbose_name_plural = "Flickr Photos"


    def __str__(self):
        return self.title if self.title else f"Photo {self.id}"
