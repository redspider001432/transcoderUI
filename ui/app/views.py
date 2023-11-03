from django.shortcuts import render ,redirect
import subprocess
from .forms import ChannelForm

def homepage(request):
    return render(request,'home.html')
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




# def execute_command(request):
#     if request.method == 'POST':
#         form = CommandForm(request.POST)
#         if form.is_valid():
#             channel_name = form.cleaned_data['channel_name']
#             command = form.cleaned_data['command']


#             try:
#                 result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
#             except subprocess.CalledProcessError as e:
#                 result = e.output

#             return render(request, 'result.html',{'channel_name':channel_name,'result':result})
#         else:
#             form = CommandForm()

#         return render(request, 'execute_command.html',{'form':form})