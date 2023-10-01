from rest_framework.routers import DefaultRouter
from .views import UserSubscriptionViewset
from django.urls import path, include


router = DefaultRouter()
router.register('user-subscription', UserSubscriptionViewset,
                basename='user-subscription')

urlpatterns = [
    path('', include(router.urls))
]
