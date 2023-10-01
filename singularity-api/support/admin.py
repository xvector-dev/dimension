from django.contrib import admin
from .models import SupportTicket, SupportTicketReply


admin.site.register(SupportTicket)
admin.site.register(SupportTicketReply)
