# -*- coding: utf-8 -*-
from django.db import models

from blog.models import Post
from core.models import TimeStampedModel


class Photo(TimeStampedModel, models.Model):
    image = models.ImageField(upload_to="%Y/%m/%d")
    post = models.ForeignKey(Post, related_name='photos')

