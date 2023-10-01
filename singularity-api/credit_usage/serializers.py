from rest_framework.serializers import ModelSerializer
from .models import UserCredit


class UserCreditSerializer(ModelSerializer):

    class Meta:
        model = UserCredit
        fields = "__all__"
