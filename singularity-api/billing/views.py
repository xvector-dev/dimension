from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import UsageRecord
from .serializers import UsageRecordSerializer


class UsageRecordViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UsageRecordSerializer

    def get_queryset(self):
        data = UsageRecord.objects.all()
        return data

    def list(self, request, *args, **kwargs):
        user = request.user
        data = UsageRecord.objects.get(user=user)
        serializer = UsageRecordSerializer(data)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user

        usage_record = UsageRecord.objects.create(user=user, record_id=data['id'],
                                                  object=data['object'], livemode=True if data['livemode'] == 'true' else False,
                                                  quantity=data['quantity'], subscription_item=data['subscription_item'], timestamp=data['timestamp'])
        usage_record.save()

        serializer = UsageRecordSerializer(usage_record)

        return Response(serializer.data)
