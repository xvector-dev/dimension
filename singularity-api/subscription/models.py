from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSubscription(models.Model):
    user = models.OneToOneField(
        User, related_name='subscription', on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=500)
    stripe_subscription_id = models.CharField(max_length=500)
    items = models.ManyToManyField('SubscriptionItems', blank=True)
    stripe_current_period_end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.first_name


class SubscriptionItems(models.Model):
    name = models.CharField(max_length=300, default='')
    description = models.CharField(max_length=500, default='')
    price = models.DecimalField(max_digits=8, decimal_places=5, default=0.009)
    subscription_item_id = models.CharField(max_length=100, default='')
    stripe_price_id = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    product = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
