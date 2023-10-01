from django.db import models


class DefaultSysPrompt(models.Model):
    tool = models.CharField(max_length=100, default="conversation")
    sys_prompt = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.tool
