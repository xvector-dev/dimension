from rest_framework.viewsets import ModelViewSet
from .serializers import ConversationSerializer, DialogMessageSerializer
from .models import Conversation, DialogMessage
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


def save_conversation(user: object, conversation_uuid: str = None, prompt: str = "", conversation_dict: dict = None):

    try:
        conversation = Conversation.objects.get(uuid_slug=conversation_uuid)
    except Exception as e:
        print(e)
        title = prompt if len(prompt) < 50 else prompt[0:49]
        conversation = Conversation.objects.create(
            user=user, title=title)
        conversation.save()
    if conversation_dict:
        user_message = DialogMessage.objects.create(
            conversation=conversation, role='user', content=prompt)

        user_message.save()

        ai_response = DialogMessage.objects.create(
            conversation=conversation, role=conversation_dict['role'], content=conversation_dict['content'])

        ai_response.save()

    return str(conversation.uuid_slug)


class ConversationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ConversationSerializer

    def get_queryset(self):
        data = Conversation.objects.all()
        return data

    def list(self, request, *args, **kwargs):
        user = request.user
        data = Conversation.objects.filter(user=user)
        serializer = ConversationSerializer(data, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        params = kwargs['pk']

        if params.isdigit():
            data = self.get_object()
            serializer = ConversationSerializer(data)

        else:
            data = Conversation.objects.get(uuid_slug=params)
            serializer = ConversationSerializer(data)

        return Response(serializer.data)
