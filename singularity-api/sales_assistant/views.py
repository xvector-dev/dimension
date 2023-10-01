from rest_framework.viewsets import ModelViewSet
from .serializers import SalesConversationSerializer, SalesDialogMessageSerializer
from .models import SalesConversation, SalesDialogMessage
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


def save_sales_conversation(user: object, conversation_uuid: str = None, prompt: str = "", conversation_dict: dict = None):

    try:
        conversation = SalesConversation.objects.get(
            uuid_slug=conversation_uuid)
    except Exception as e:
        print(e)
        title = prompt if len(prompt) < 50 else prompt[0:49]
        conversation = SalesConversation.objects.create(
            user=user, title=title)
        conversation.save()
    if conversation_dict:
        user_message = SalesDialogMessage.objects.create(
            sales_conversation=conversation, role='user', content=prompt)

        user_message.save()

        ai_response = SalesDialogMessage.objects.create(
            sales_conversation=conversation, role=conversation_dict['role'], content=conversation_dict['content'])

        ai_response.save()

    return str(conversation.uuid_slug)


class SalesConversationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SalesConversationSerializer

    def get_queryset(self):
        data = SalesConversation.objects.all()
        return data

    def list(self, request, *args, **kwargs):
        user = request.user
        data = SalesConversation.objects.filter(user=user)
        serializer = SalesConversationSerializer(data, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        params = kwargs['pk']

        if params.isdigit():
            data = self.get_object()
            serializer = SalesConversationSerializer(data)

        else:
            data = SalesConversation.objects.get(uuid_slug=params)
            serializer = SalesConversationSerializer(data)

        return Response(serializer.data)
