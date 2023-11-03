from django import forms

class ChannelForm(forms.Form):
    channel_name = forms.CharField(label='Channel Name', max_length=100)
    hls_stream_url = forms.URLField(label='HLS Stream URL')
