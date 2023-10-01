from rest_framework.serializers import ModelSerializer
from .models import YouTubeConversation, YouTubeDialogMessage


class YouTubeDialogMessageSerializer(ModelSerializer):

    class Meta:
        model = YouTubeDialogMessage
        fields = "__all__"


class YouTubeConversationSerializer(ModelSerializer):

    youtube_dialog_messages = YouTubeDialogMessageSerializer(many=True)

    class Meta:
        model = YouTubeConversation
        fields = ['id', 'title', 'uuid_slug',
                  'created_at', 'youtube_dialog_messages']
