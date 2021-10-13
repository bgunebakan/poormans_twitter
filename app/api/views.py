from rest_framework import viewsets
from api.models import Tweet
from api.serializers import TweetSerializer


class TweetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tweets to be listed or created.
    """
    queryset = Tweet.objects.all().order_by('-created_at')
    serializer_class = TweetSerializer
