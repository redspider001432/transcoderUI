from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('add_channel',views.add_channel,name='add_channel'),
    path('edit_channel',views.edit_channel,name='edit_channel')
]
