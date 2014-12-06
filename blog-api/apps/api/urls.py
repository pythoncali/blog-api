# -*- coding: utf-8 -*-
from django.conf.urls import patterns

from rest_framework import routers


from users.api_views import UserViewSet
from blog.api_views import PostViewSet

router = routers.SimpleRouter()

router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = patterns('',)

urlpatterns = router.urls
