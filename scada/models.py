from django.db import models


class DeviceRTU(models.Model):
    addr = models.IntegerField()
    reg = models.IntegerField()
    type = models.CharField(max_length=8)  # bool, integer
    base = models.IntegerField()  # основание(множетель) для перевода к действ. числу
    enable_online = models.BooleanField()
    enable_archive = models.BooleanField()
    interval_online = models.IntegerField()  # ms
    interval_archive = models.IntegerField()  # ms


class OnlineRTU(models.Model):
    device_id = models.OneToOneField(DeviceRTU)
    value = models.IntegerField()


class ArchiveRTU(models.Model):
    device_id = models.OneToOneField(DeviceRTU)
    time_value = models.DateTimeField()  # значение даты время опроса
    value = models.IntegerField()
