from rest_framework.routers import DefaultRouter
from .views import CodeConversationViewSet
from django.urls import path, include


router = DefaultRouter()
router.register('code-conversation', CodeConversationViewSet,
                basename='code-conversation')


urlpatterns = [
    path('', include(router.urls))
]
