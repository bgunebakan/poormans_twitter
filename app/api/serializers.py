from rest_framework import serializers
from api.models import Tweet


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'name', 'tweet', 'created_at']
