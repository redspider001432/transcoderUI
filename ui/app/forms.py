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

class ChannelForm(forms.Form):
    channel_name = forms.CharField(label='Channel Name', max_length=100)
    udp_stream = forms.CharField(label='UDP Stream')
    video_codec = forms.ChoiceField(label='Video Codec',choices=VIDEO_CHOICES)
    audio_codec = forms.ChoiceField(label='Audio Codec',choices=AUDIO_CHOICES)
    preset = forms.ChoiceField(label='Select Preset', choices=PRESET_CHOICES, required=True)
    video_bitrate = forms.IntegerField(label='Video Bitrate',min_value='0',max_value='6000')
    resolution = forms.CharField(label='Resolution',max_length=100)