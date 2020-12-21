from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(allow_unicode=True)
    main_image = models.ImageField(upload_to='posts/')
    image1 = models.ImageField(upload_to='posts/', null=True, blank=True)
    image2 = models.ImageField(upload_to='posts/', null=True, blank=True)
    image3 = models.ImageField(upload_to='posts/', null=True, blank=True)
    body = RichTextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Post"
