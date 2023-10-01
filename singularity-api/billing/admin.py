from django.contrib import admin
from .models import TotalMonthlyBilling, TotalMonthlyImageUsage, TotalMonthlyLLMUsage, UsageRecord

admin.site.register(TotalMonthlyBilling)
admin.site.register(TotalMonthlyImageUsage)
admin.site.register(TotalMonthlyLLMUsage)
admin.site.register(UsageRecord)
