from rest_framework.serializers import ModelSerializer
from .models import GeneratedImage
from users.serializers import CustomUserSerializer


class GeneratedImageSerializer(ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = GeneratedImage
        fields = ['id', 'user', 'image_prompt', 'image_name', 'image_type',
                  'image_size', 'image', 'public', 'created_at']
