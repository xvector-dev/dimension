from rest_framework.routers import DefaultRouter
from .views import YouTubeConversationViewSet
from django.urls import path, include


router = DefaultRouter()
router.register('youtube-conversation', YouTubeConversationViewSet,
                basename='youtube-conversation')


urlpatterns = [
    path('', include(router.urls))
]
