from rest_framework.viewsets import ModelViewSet
from .serializers import CodeConversationSerializer, CodeDialogMessageSerializer
from .models import CodeConversation, CodeDialogMessage
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


def save_code_conversation(user: object, conversation_uuid: str = None, prompt: str = "", conversation_dict: dict = None):

    try:
        conversation = CodeConversation.objects.get(
            uuid_slug=conversation_uuid)
    except Exception as e:
        print(e)
        title = prompt if len(prompt) < 50 else prompt[0:49]
        conversation = CodeConversation.objects.create(
            user=user, title=title)
        conversation.save()
    if conversation_dict:
        user_message = CodeDialogMessage.objects.create(
            code_conversation=conversation, role='user', content=prompt)

        user_message.save()

        ai_response = CodeDialogMessage.objects.create(
            code_conversation=conversation, role=conversation_dict['role'], content=conversation_dict['content'])

        ai_response.save()

    return str(conversation.uuid_slug)


class CodeConversationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CodeConversationSerializer

    def get_queryset(self):
        data = CodeConversation.objects.all()
        return data

    def list(self, request, *args, **kwargs):
        user = request.user
        data = CodeConversation.objects.filter(user=user)
        serializer = CodeConversationSerializer(data, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        params = kwargs['pk']

        if params.isdigit():
            data = self.get_object()
            serializer = CodeConversationSerializer(data)

        else:
            data = CodeConversation.objects.get(uuid_slug=params)
            serializer = CodeConversationSerializer(data)

        return Response(serializer.data)
