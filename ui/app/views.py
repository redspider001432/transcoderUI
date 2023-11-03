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
            udp_stream = form.cleaned_data['udp_stream']
            preset = form.cleaned_data['preset']
            bash_command = f"{channel_name} {udp_stream} {preset}"

            try:
                subprocess.run(bash_command,shell=True,check=True)
                return redirect('home.html')
            except subprocess.CalledProcessError as e:
                return -1
    else:
        form = ChannelForm()
    return render(request,'add_channel_form.html',{'form':form})

def edit_channel(request):
    pass