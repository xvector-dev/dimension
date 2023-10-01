"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('users.urls')),
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(),
    #      name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
    #      name='token_refresh'),
    path('subscriptions/', include('subscription.urls')),
    path('credit-usage/', include('credit_usage.urls')),
    path('billing/', include('billing.urls')),
    path('llama/', include('llama.urls')),
    path('conversations/', include('conversation.urls')),
    path('code-assistant/', include('code_assistant.urls')),
    path('sales-assistant/', include('sales_assistant.urls')),
    path('youtube-assistant/', include('youtube_assistant.urls')),
    path('generated-images/', include('image_generator.urls')),
    path('support/', include('support.urls')),
]
