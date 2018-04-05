import pymongo
from django.conf import settings


class BaseModel:
    """
       a simple base class to make it easier to work with
       mongodb collections and databses.
    """
 
    collection = ""

    def __init__(self):
        self._conn = settings.MONGO
        self.db = settings.DB

    @property
    def objects(self):
        assert self.collection, "No collection specified."
        return self.db[self.collection]
    
    def normalize_data(self, data):
        '''used to normalize data or add custom fields if needed'''
        return data

    def save(self, data, many=False, ordered=False):
        '''
            insert many or one document into a collection

            params:
                - data: actual data to insert
                - many: specifies if the data is a list or a single dict
                - ordered: insert data in arbitary order, used with insert_many
                           to specifiy if data inserted in aribitary order and fail
                           on the first insert failiar
            returns:
                - a list or single instance of ObjectId
        '''
        try:
            if many and isinstance(data, list):
                data = [self.normalize_data(entry) for entry in data]
                return self.objects.insert_many(data, ordered=ordered)
            else:
                data = self.normalize_data(data)
                return self.objects.insert_one(data)
        
        except pymongo.errors.DuplicateKeyError:
            return False  # this might not be the right choice, will find out!!!


class Feed(BaseModel):
    '''Represents a feed of tweets'''

    collection = "feed"

    def normalize_data(self, data):
        '''
            append user screen_name as "handle" to top level of tweet
            to help query the feed based on user handle
        '''
        user = data.get('user', None)
        if user:
            data['handle'] = user['screen_name']

        return data

