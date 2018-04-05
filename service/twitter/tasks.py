import pymongo
from django.conf import settings
from celery import shared_task
from celery.utils.log import get_task_logger

from twitter.api import Fetcher
from twitter.models import Feed


logger = get_task_logger(__name__)


@shared_task(name='update_feed')
def update_twitter_feed(handle, count=settings.MAX_TWEETS_COUNT):
    '''
       celery task to retrive latest tweets by a user
       and store them in a mongo 'feed' collection.
    '''
    twitter = Fetcher()
    feed = Feed()

    # returns latest entry in feed collection as it should be indexed using tweet id.
    most_recent = feed.objects.find_one(filter={'handle': handle}, sort=[('id', -1)])
    if most_recent:
        data = twitter.get_feed(handle, since_id=most_recent['id'], count=count)
    else:
        data = twitter.get_feed(handle, count=count)

    try:
        if data:
            inserted = feed.save(data, many=True)
            logger.debug("inserted: {}".format(inserted))
    except pymongo.errors.BulkWriteError as e:
        logger.warning("Faild to save feed, faild bulk operations {}".format(e.details))

    return data
