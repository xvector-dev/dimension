from django.contrib import admin
from .models import Conversation, DialogMessage

admin.site.register(Conversation)
admin.site.register(DialogMessage)
