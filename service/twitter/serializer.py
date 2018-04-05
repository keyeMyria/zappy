'''
  Basic simple Sreializer for use with pymongo
'''
from rest_framework import serializers

from twitter.tasks import update_twitter_feed


class FeedSerializer:
    '''
      a dummy simple serializer for tweets
      it only needs to return a list of data
      from a pymongo cursor.
    '''
    def __init__(self, cursor, many=False):
        self.cursor = cursor
        self.many = many
    
    @property
    def data(self):
        return [tweet for tweet in self.cursor]


class FeedFetchActionSerializer(serializers.Serializer):
    '''serves as simple validating form of a sort'''
    
    handle = serializers.CharField(required=True)
    count = serializers.IntegerField(required=False)
    
    def save(self):
        if self.is_valid():
            handle = self.validated_data['handle']
            count = self.validated_data['count']
            update_twitter_feed.delay(handle, count)
