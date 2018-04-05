import logging

import pymongo
from django.conf import settings
from birdy import twitter

from twitter.models import Feed


class Fetcher:
    '''Fetch data from Twitter API with no fuss.'''
    
    def __init__(self):
        self.client = twitter.AppClient(
            consumer_key=settings.TWITTER_CONSUMER_KEY,
            consumer_secret=settings.TWITTER_CONSUMER_SECRET,
        )
        self.db = settings.DB
        self.session = self.db.get_collection('session')
        
        self.logger = logging.getLogger(__name__)

    def get_access_token(self, valid=True):
        '''
            authenticate the client by retriving a stored access_token
            or fetching a new one if it's not valid or not found.
        '''
        session = self.db.get_collection('session')
        
        token = session.find_one({'access_token': {'$exists': True}})
        
        if token and valid:
            self.client.access_token = token['access_token']
            self.client.session = self.client.get_oauth_session()

        if not token or not valid:
            token = self.client.get_access_token()
            session.replace_one(
                {'access_token': {'$exists': True}}, 
                {'access_token': token},
                upsert=True,
            )
    
    def get_feed(self, handle, since_id=None, count=200):
        '''
            retrive user_timeline tweets from twitter
            and handle access_token invalidation.
        '''
        self.get_access_token()
        
        try:
            res = self.client.api.statuses.user_timeline.get(
                screen_name=handle, 
                count=count, 
                since_id=since_id,
            )
        except twitter.TwitterAuthError:
            self.get_access_token(valid=False)

            # try again
            res = self.client.api.statuses.user_timeline.get(screen_name=handle)
        
        return res.data
