from django import forms
PRESET_CHOICES = [
    ('slow', 'slow'),
    ('fast', 'fast'),
    ('veryfast', 'veryfast'),
]
VIDEO_CHOICES =[
    ('libx264','libx264'),
    ('mpeg2video','mpeg2video'),
    ('mpeg4','mpeg4')
]
AUDIO_CHOICES =[
    ('aac','aac'),
    ('aac3','aac3'),
    ('mp2','mp2'),
    ('mp3','mp3')
]
RESOLUTION_CHOICES = [
    ('720:480','SD'),
    ('1280:720','HD'),
    ('1920:1080','Full HD')
]
class ChannelForm(forms.Form):
    channel_name = forms.CharField(label='Channel Name', max_length=100)
    stream = forms.CharField(label='Input Stream',max_length=100)
    video_codec = forms.ChoiceField(label='Video Codec',choices=VIDEO_CHOICES)
    audio_codec = forms.ChoiceField(label='Audio Codec',choices=AUDIO_CHOICES)
    preset = forms.ChoiceField(label='Select Preset', choices=PRESET_CHOICES, required=True)
    video_bitrate = forms.IntegerField(label='Video Bitrate',min_value=0,max_value=5000)
    resolution = forms.ChoiceField(label='Resolution',choices=RESOLUTION_CHOICES)
    output_url = forms.CharField(label='Output Stream',max_length=50)