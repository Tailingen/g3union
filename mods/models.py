from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Mod.Status.PUBLISHED)


class Mod(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовать'

    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    desc = models.TextField(blank=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='mods')
    tags = models.ManyToManyField('Tag', blank=True)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = 'Моды'
        verbose_name_plural = 'Моды'
        ordering = ['-created']
        indexes = [models.Index(fields=['-created'])]

    def get_absolute_url(self):
        return reverse('show_post', kwargs={'post_slug': self.slug})

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

cats_list = Category.objects.all()

def list_cat(request):
    return {'cats': Category.objects.all()}

class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

tags_list = Tag.objects.all()
