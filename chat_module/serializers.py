from django.utils.text import slugify
from rest_framework import serializers
from shortuuidfield import ShortUUIDField

from accounts_module.serializers import UserViewSerializer
from chat_module.models import ChatRoom


class ChatRoomSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False, read_only=True)
    member = UserViewSerializer(many=True, read_only=True)
    members = serializers.ListField(write_only=True)

    def create(self, validated_data):
        member_object = validated_data.pop('members')
        chat_room = ChatRoom.objects.create(**validated_data)
        chat_room.member.set(member_object)
        return chat_room



    class Meta:
        model = ChatRoom
        exclude = ['id']
