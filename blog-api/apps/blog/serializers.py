# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # author = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='title'
    # )

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'body', 'author',)
        write_only_fields = ('author',)
        read_only_fields = ('slug',)