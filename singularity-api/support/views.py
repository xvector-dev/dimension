from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponseNotFound
from .models import SupportTicket, SupportTicketReply
from .serializers import SupportTicketSerializer, SupportTicketReplySerializer


class SupportTicketViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SupportTicketSerializer

    def get_queryset(self):
        data = SupportTicket.objects.all()
        return data

    def list(self, request, *args, **kwargs):
        user = request.user
        try:
            data = SupportTicket.objects.filter(author=user)
            serializer = SupportTicketSerializer(data, many=True)
            return Response(serializer.data)
        except:
            return HttpResponseNotFound()

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        ticket = SupportTicket.objects.create(
            author=user, title=data['title'], content=data['content'])
        ticket.save()

        serializer = SupportTicketSerializer(ticket)

        return Response(serializer.data)


class SupportTicketReplyViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SupportTicketReplySerializer

    def get_queryset(self):
        data = SupportTicketReply.objects.all()
        return data

    def list(self, request, *args, **kwargs):
        user = request.user
        try:
            data = SupportTicketReply.objects.filter(author=user)
            serializer = SupportTicketReplySerializer(data, many=True)
            return Response(serializer.data)
        except:
            return HttpResponseNotFound()

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        ticket = SupportTicket.objects.get(id=data['ticket_id'])

        ticket_reply = SupportTicketReply.objects.create(
            ticket=ticket, author=user, content=data['content'])
        ticket_reply.save()

        serializer = SupportTicketReplySerializer(ticket_reply)

        return Response(serializer.data)
