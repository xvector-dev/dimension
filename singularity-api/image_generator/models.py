from django.db import models
from users.models import UserAccount


def generate_filename(self, filename):
    path = f"files/generated_images/{self.user.first_name}-{self.user.last_name}/{filename}"

    return path


class GeneratedImage(models.Model):
    user = models.ForeignKey(
        UserAccount, related_name="generated_images", on_delete=models.CASCADE)
    image_prompt = models.CharField(max_length=5000, default='')
    image_name = models.CharField(max_length=500)
    image_type = models.CharField(max_length=10)
    image_size = models.CharField(max_length=50)
    image = models.ImageField(upload_to=generate_filename)
    public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.image_name} --- {self.image_size}"

    class Meta:
        ordering = ["-created_at"]
