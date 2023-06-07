from django.urls import path, re_path

from . import views


app_name = 'chat'
urlpatterns = [
    # re_path(r'(?P<slug>[-\w]+)/', views.ChatRoomView.as_view(), name='chat_room'),
    path('', views.ChatRoomView.as_view(), name='chat_room'),
]

