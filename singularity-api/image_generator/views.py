from rest_framework.viewsets import ModelViewSet
from .models import GeneratedImage
from .serializers import GeneratedImageSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests
import secrets
import string
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile


class GeneratedImageViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GeneratedImageSerializer

    def get_queryset(self):
        data = GeneratedImage.objects.all()
        return data

    def list(self, request, *args, **kwargs):
        user = request.user
        data = GeneratedImage.objects.filter(user=user)
        serializer = GeneratedImageSerializer(data, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        params = kwargs['pk']

        if params.isdigit():
            data = self.get_object()
            serialzer = GeneratedImageSerializer(data)

        else:
            if params == 'shared':
                data = GeneratedImage.objects.filter(public=True)
                serialzer = GeneratedImageSerializer(data, many=True)

        return Response(serialzer.data)

    def download_image(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful
            content_length = response.headers.get("Content-Length")

            # Convert the content length to an integer
            image_size = int(content_length) / 1000000

            return response.content, str(round(image_size, 2))
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def generate_image_name(self):
        # Includes uppercase letters, lowercase letters, and digits
        alphabet = string.ascii_letters + string.digits
        name = ''.join(secrets.choice(alphabet) for _ in range(10))
        return name

    def convert_image_for_django(self, image, image_name, image_type):
        # Create a Django ContentFile from the binary image data
        image_content = ContentFile(
            content=image, name=f"{image_name}.{image_type}")

        # # Create a Django SimpleUploadedFile from the ContentFile
        converted_image = SimpleUploadedFile(
            image_content.name, image_content.read(), content_type=f"image/{image_type}")

        return converted_image

    def create(self, request, *args, **kwargs):
        data = request.data
        image_url = data['image_url']
        image_prompt = data['image_prompt']
        image, image_size = self.download_image(image_url)
        image_name = self.generate_image_name()
        image_type = 'png'

        converted_image = self.convert_image_for_django(
            image, image_name, image_type)

        new_image = GeneratedImage.objects.create(
            user=request.user, image_prompt=image_prompt, image_name=image_name, image_type=image_type, image_size=image_size, image=converted_image)

        new_image.save()

        serializer = GeneratedImageSerializer(new_image)
        return Response(serializer.data)
