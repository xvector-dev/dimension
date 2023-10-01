from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCredit(models.Model):
    user = models.OneToOneField(
        User, related_name="user_credit", on_delete=models.CASCADE)
    credit_value = models.DecimalField(
        max_digits=5, decimal_places=3, default=5)
    credit_usage = models.DecimalField(
        max_digits=5, decimal_places=3, default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.email
