from rest_framework.routers import DefaultRouter
from .views import SalesConversationViewSet
from django.urls import path, include


router = DefaultRouter()
router.register('sales-conversation', SalesConversationViewSet,
                basename='sales-conversation')


urlpatterns = [
    path('', include(router.urls))
]
