from rest_framework.serializers import ModelSerializer
from .models import Conversation, DialogMessage


class DialogMessageSerializer(ModelSerializer):

    class Meta:
        model = DialogMessage
        fields = "__all__"


class ConversationSerializer(ModelSerializer):

    dialog_messages = DialogMessageSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ['id', 'title', 'uuid_slug', 'created_at', 'dialog_messages']
