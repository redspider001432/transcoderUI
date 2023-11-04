from django.shortcuts import render ,redirect
import subprocess
from .forms import ChannelForm
from .models import Channels
def homepage(request):
    channels = Channels.objects.all()
    return render(request,'home.html',{'channels':channels})
def add_channel(request):
    if request.method == 'POST':
        form = ChannelForm(request.POST)
        if form.is_valid():
            channel_name = form.cleaned_data['channel_name']
            stream = form.cleaned_data['stream']
            preset = form.cleaned_data['preset']
            video_codec = form.cleaned_data['video_codec']
            audio_codec = form.cleaned_data['audio_codec']
            video_bitrate = form.cleaned_data['video_bitrate']
            resolution = form.cleaned_data['resolution']
            output_url = form.cleaned_data['output_url']
            bash_command = f"ffmpeg -i {stream} -acodec {audio_codec} -vcodec {video_codec} -preset {preset} -vb {video_bitrate}k -vf scale={resolution} -f mpegts {output_url} &"

            try:
                subprocess.run(bash_command,shell=True,check=True)
                channels = Channels(
                    channel_name = channel_name,
                    preset = preset,
                    stream = stream,
                    video_codec = video_codec,
                    audio_codec = audio_codec,
                    video_bitrate = video_bitrate,
                    resolution = resolution,
                    output_url = output_url
                )
                channels.save()
                return redirect('home.html')
            except subprocess.CalledProcessError as e:
                return -1
    else:
        form = ChannelForm()
    return render(request,'add_channel_form.html',{'form':form})

def edit_channel(request):
    pass