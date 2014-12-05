# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils.encoding import python_2_unicode_compatible

from core.models import TimeStampedModel


@python_2_unicode_compatible
class Post(TimeStampedModel, models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)