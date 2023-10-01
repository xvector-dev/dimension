from rest_framework.routers import DefaultRouter
from .views import UserCreditViewset
from django.urls import path, include


router = DefaultRouter()
router.register('user-credit', UserCreditViewset, basename='user-credit')

urlpatterns = [
    path('', include(router.urls))
]
