from django.contrib import admin
from .models import UserSubscription, SubscriptionItems

admin.site.register(UserSubscription)
admin.site.register(SubscriptionItems)
