from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UsageRecordViewset

router = DefaultRouter()
router.register('usage-record', UsageRecordViewset, basename='usage-record')

urlpatterns = [
    path('', include(router.urls))
]
