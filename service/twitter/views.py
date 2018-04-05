from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from twitter.models import Feed
from twitter.tasks import update_twitter_feed
from twitter.serializer import FeedSerializer, FeedFetchActionSerializer


class TwitterFeedViewSet(viewsets.ViewSet):
    '''
       a simple viewset for listing feed tweets
       and providing an slack command action.
    '''
    
    model = Feed()
    serializer_class = FeedSerializer
    fields = {'_id': False,'id': False}
    ordering = [('id', -1)]
    
    def get_queryset(self):
        handle = self.request.query_params.get('handle', None)
        query = {}
        
        if handle:
            # can pass the whole request.query_param but it's cleaner this way
            query = {'handle': handle.lower()}

        return self.model.objects.find(
            filter=query, projection=self.fields, sort=self.ordering,
        )

    def list(self, request):
        '''
          retrive a list of tweets from feed collection
        '''
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def fetch(self, request):
        '''
          fetch twitter user timeline in a background task
          mainly used as a slack command endpoint.
        '''
        serializer = FeedFetchActionSerializer(data=request.data)
        serializer.save()

        return Response(status=status.HTTP_200_OK)
