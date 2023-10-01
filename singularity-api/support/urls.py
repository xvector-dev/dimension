from rest_framework.routers import DefaultRouter
from .views import SupportTicketViewset, SupportTicketReplyViewset
from django.urls import path, include


router = DefaultRouter()
router.register('ticket', SupportTicketViewset, basename='ticket')
router.register('ticket-reply', SupportTicketReplyViewset,
                basename='ticket-reply')


urlpatterns = [
    path('', include(router.urls))
]
