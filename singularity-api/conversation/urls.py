from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet
from django.urls import path, include


router = DefaultRouter()
router.register('conversation', ConversationViewSet, basename='conversation')


urlpatterns = [
    path('', include(router.urls))
]
