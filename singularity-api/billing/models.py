from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class TotalMonthlyBilling(models.Model):
    user = models.ForeignKey(
        User, related_name="monthly_billing", on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=8, decimal_places=5)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.first_name


class TotalMonthlyImageUsage(models.Model):
    user = models.ForeignKey(
        User, related_name="image_monthly_usage", on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=8, decimal_places=5)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.first_name


class TotalMonthlyLLMUsage(models.Model):
    user = models.ForeignKey(
        User, related_name="llm_monthly_usage", on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=8, decimal_places=5)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.first_name


class UsageRecord(models.Model):
    user = models.ForeignKey(
        User, related_name="usage_record", on_delete=models.CASCADE)
    record_id = models.CharField(max_length=300)
    object = models.CharField(max_length=300)
    livemode = models.BooleanField()
    quantity = models.IntegerField(default=1)
    subscription_item = models.CharField(max_length=300)
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.first_name
