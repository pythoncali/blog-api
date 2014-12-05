# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models library
from django.db import models

from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    followers = models.ManyToManyField('self', related_name='followers', symmetrical=False)

    def __unicode__(self):
        return self.username
