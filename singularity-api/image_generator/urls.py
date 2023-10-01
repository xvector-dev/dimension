from rest_framework.routers import DefaultRouter
from .views import GeneratedImageViewset
from django.urls import path, include

router = DefaultRouter()
router.register('generated-image', GeneratedImageViewset,
                basename='generated-image')

urlpatterns = [
    path('', include(router.urls))
]
