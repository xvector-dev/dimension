from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponseNotFound
from .serializers import UserCreditSerializer
from .models import UserCredit
from decimal import Decimal


class UserCreditViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserCreditSerializer

    def get_queryset(self):
        data = UserCredit.objects.all()
        return data

    def list(self, request, *args, **kwargs):
        user = request.user
        try:
            data = UserCredit.objects.get(user=user)
            serializer = UserCreditSerializer(data)

            return Response(serializer.data)
        except:
            return HttpResponseNotFound()

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        user_credit = UserCredit.objects.create(user=user)
        user_credit.save()

        serializer = UserCreditSerializer(user_credit)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        data = request.data

        user_credit = self.get_object()
        usage = user_credit.credit_usage + Decimal(data['credit_usage'])
        if usage > user_credit.credit_value:
            user_credit.credit_usage = user_credit.credit_value
            user_credit.active = False
        else:
            user_credit.credit_usage = usage

        user_credit.save()

        serializer = UserCreditSerializer(user_credit)

        return Response(serializer.data)
