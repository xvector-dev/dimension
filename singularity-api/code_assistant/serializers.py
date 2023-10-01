from rest_framework.serializers import ModelSerializer
from .models import CodeConversation, CodeDialogMessage


class CodeDialogMessageSerializer(ModelSerializer):

    class Meta:
        model = CodeDialogMessage
        fields = "__all__"


class CodeConversationSerializer(ModelSerializer):

    code_dialog_messages = CodeDialogMessageSerializer(many=True)

    class Meta:
        model = CodeConversation
        fields = ['id', 'title', 'uuid_slug',
                  'created_at', 'code_dialog_messages']
