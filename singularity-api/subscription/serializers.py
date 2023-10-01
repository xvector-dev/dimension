from rest_framework.serializers import ModelSerializer
from .models import UserSubscription


class UserSubscriptionSerializer(ModelSerializer):

    class Meta:
        model = UserSubscription
        fields = "__all__"
