from django.contrib import admin
from .models import DeviceRTU, OnlineRTU, ArchiveRTU


admin.site.register(DeviceRTU)
admin.site.register(OnlineRTU)
admin.site.register(ArchiveRTU)
