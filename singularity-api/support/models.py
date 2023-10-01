from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class SupportTicket(models.Model):
    author = models.ForeignKey(
        User, related_name="support_ticket", on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField(max_length=1000)
    category = models.CharField(max_length=100, default='support')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-created_at"]


class SupportTicketReply(models.Model):
    ticket = models.ForeignKey(
        SupportTicket, related_name="support_ticket_reply", on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, related_name="support_ticket_reply", on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"reply to {self.ticket.title}"

    class Meta:
        ordering = ["-created_at"]
