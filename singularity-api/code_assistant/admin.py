from django.contrib import admin
from .models import CodeConversation, CodeDialogMessage


admin.site.register(CodeConversation)
admin.site.register(CodeDialogMessage)
