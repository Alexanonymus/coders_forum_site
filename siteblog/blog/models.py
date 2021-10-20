from django.db import models
from django.urls import reverse

'''
Category
=========
title, slug

Tag
========
title, slug

Post
=========
title, slug, author, content, photo, created_at, views, category, tags

'''

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name="Url", unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self,):
        return reverse('category', kwargs={"slug":self.slug})

    class Meta:
        ordering = ['title']

class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, verbose_name="Url", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name="Url", unique=True)
    author = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Chop qilingan vaqti')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    views = models.IntegerField(default=0,verbose_name='Ko`rishlar soni')
    category = models.ForeignKey(Category, on_delete=models.PROTECT,related_name='posts')
    tags = models.ManyToManyField(Tag,blank=True, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self, ):
        return reverse('post', kwargs={"slug": self.slug})
