from django.contrib import admin
from .models import UserAccount, UserDetails, ProfileImage

admin.site.register(UserAccount)
admin.site.register(UserDetails)
admin.site.register(ProfileImage)
