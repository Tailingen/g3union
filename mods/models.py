from django.db import models
from django.urls import reverse


class Mod(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    desc = models.TextField(blank=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='mods')
    tags = models.ManyToManyField('Tag', blank=True)

    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created'])]

    def get_absolute_url(self):
        return reverse('show_post', kwargs={'slug': self.slug})

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

cats_list = Category.objects.all()

def list_cat(request):
    return {'cats': Category.objects.all()}

class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title
