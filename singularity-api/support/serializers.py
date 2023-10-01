from rest_framework.serializers import ModelSerializer
from .models import SupportTicket, SupportTicketReply
from users.serializers import CustomUserSerializer


class SupportTicketReplySerializer(ModelSerializer):
    author = CustomUserSerializer()

    class Meta:
        model = SupportTicketReply
        fields = ["ticket", "author", "content", "created_at"]


class SupportTicketSerializer(ModelSerializer):

    support_ticket_reply = SupportTicketReplySerializer(many=True)

    class Meta:
        model = SupportTicket
        fields = ["id", "author", "title", "content", "category",
                  "status", "created_at", "updated_at", "support_ticket_reply"]
