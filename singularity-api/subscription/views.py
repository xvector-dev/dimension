from rest_framework.viewsets import ModelViewSet
from .models import UserSubscription, SubscriptionItems
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSubscriptionSerializer
from django.http import HttpResponseNotFound
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSubscriptionViewset(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserSubscriptionSerializer

    def get_queryset(self):
        data = UserSubscription.objects.all()
        return data

    def list(self, request, *args, **kwargs):
        try:
            user = request.user
            data = UserSubscription.objects.get(user=user)
            serializer = UserSubscriptionSerializer(data)
            return Response(serializer.data)
        except:
            return HttpResponseNotFound()

    def create(self, request, *args, **kwargs):
        data = request.data

        user = User.objects.get(id=data['userId'])
        user_subscription = UserSubscription.objects.create(
            user=user, stripe_customer_id=data['stripeCustomerId'],
            stripe_subscription_id=data['stripeSubscriptionId'],
            stripe_current_period_end=data['stripeCurrentPeriodEnd'])

        user_subscription.save()

        if "items" in data:
            for item in data['items']:
                sub_items = SubscriptionItems.objects.get(
                    stripe_price_id=item['id'])
                user_subscription.items.add(sub_items)

        serializer = UserSubscriptionSerializer(user_subscription)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        data = request.data

        user_subscription = UserSubscription.objects.get(
            stripe_subscription_id=data['stripe_subscription_id'])

        user_subscription.stripe_current_period_end = data.get(
            'stripe_current_period_end', user_subscription.stripe_current_period_end)

        user_subscription.save()

        serializer = UserSubscriptionSerializer(user_subscription)

        return Response(serializer.data)
