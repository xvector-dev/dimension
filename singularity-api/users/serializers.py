from rest_framework.serializers import ModelSerializer
from .models import ProfileImage, UserDetails
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class ProfileImageSerializer(ModelSerializer):

    class Meta:
        model = ProfileImage
        fields = ["id", "image"]


class UserDetailsSerializer(ModelSerializer):
    user = CustomUserSerializer()
    profile_image = ProfileImageSerializer()

    class Meta:
        model = UserDetails
        fields = ['id', 'user', 'profile_image',
                  'bio', 'created_at', 'updated_at']
