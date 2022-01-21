from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Categorys(models.Model):
    title = models.SlugField(max_length=32770, unique=True, help_text='Slugify', verbose_name='Name')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

class Posts(models.Model):
    title = models.CharField(max_length=510)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    icon = models.ImageField(upload_to='media')
    description = models.CharField(max_length=65535)
    category = models.CharField(max_length=32770)
    content = models.TextField()
    date = models.DateField(auto_now_add=True, editable=False)
    like = models.ManyToManyField(User, related_name='+')
    class Meta:
        ordering = ['-pk']

    def likes(self):
        return self.like.count()

    def __str__(self):
        return str(self.pk)+' ± '+self.title

    def get_absolute_url(self):
        return reverse('article', args=str(self.pk))
