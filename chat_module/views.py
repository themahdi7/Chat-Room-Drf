from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from chat_module.models import ChatRoom
from chat_module.serializers import ChatRoomSerializer


class ChatRoomView(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ChatRoomSerializer
    parser_classes = (MultiPartParser,)

    def get(self, request):
        """
        Get all chat with user id
        """

        chat_rooms = ChatRoom.objects.filter(member=request.user.id).all()
        serializer = self.serializer_class(
            chat_rooms, many=True, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = ChatRoomSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

