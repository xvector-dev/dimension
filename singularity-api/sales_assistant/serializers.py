from rest_framework.serializers import ModelSerializer
from .models import SalesConversation, SalesDialogMessage


class SalesDialogMessageSerializer(ModelSerializer):

    class Meta:
        model = SalesDialogMessage
        fields = "__all__"


class SalesConversationSerializer(ModelSerializer):

    sales_dialog_messages = SalesDialogMessageSerializer(many=True)

    class Meta:
        model = SalesConversation
        fields = ['id', 'title', 'uuid_slug',
                  'created_at', 'sales_dialog_messages']
