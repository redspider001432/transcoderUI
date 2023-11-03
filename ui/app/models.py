from django.db import models

# Create your models here.
class Channels(models.Model):
    channel_name = models.CharField(max_length=100)
    udp_stream = models.CharField(max_length=100)
    video_codec = models.CharField(max_length=100)
    audio_codec = models.CharField(max_length=100)
    preset = models.CharField(max_length=100)
    video_bitrate = models.IntegerField()
    resolution = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True, null=True)