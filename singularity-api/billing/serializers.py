from rest_framework.serializers import ModelSerializer
from .models import UsageRecord


class UsageRecordSerializer(ModelSerializer):

    class Meta:
        model = UsageRecord
        fields = "__all__"
