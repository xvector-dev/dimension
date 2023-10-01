from django.db import models
from django.contrib.auth import get_user_model
import uuid


User = get_user_model()


class CodeConversation(models.Model):
    user = models.ForeignKey(
        User, related_name='code_conversation', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(
        max_length=200, default='programming_conversation')
    uuid_slug = models.UUIDField(
        default=uuid.uuid4, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-created_at']


class CodeDialogMessage(models.Model):
    code_conversation = models.ForeignKey(
        CodeConversation, related_name='code_dialog_messages', on_delete=models.CASCADE)
    key = models.UUIDField(default=uuid.uuid4)
    role = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.code_conversation.title

    class Meta:
        ordering = ['created_at']
