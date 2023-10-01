from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CustomProviderAuthView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView,
    UserDetailsViewst,
    ProfileImageViewst
)

router = DefaultRouter()
router.register('user-details', UserDetailsViewst, basename="user-details")
router.register('profile-image', ProfileImageViewst, basename="profile-image")

urlpatterns = [
    re_path(
        r'^o/(?P<provider>\S+)/$',
        CustomProviderAuthView.as_view(),
        name='provider-auth'
    ),
    path('jwt/create/', CustomTokenObtainPairView.as_view()),
    path('jwt/refresh/', CustomTokenRefreshView.as_view()),
    path('jwt/verify/', CustomTokenVerifyView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('', include(router.urls))
]
