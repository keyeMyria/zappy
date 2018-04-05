from rest_framework.routers import DefaultRouter

from twitter.views import TwitterFeedViewSet


router = DefaultRouter()
router.register(r'feed', TwitterFeedViewSet, base_name='feed')

urlpatterns = router.urls
