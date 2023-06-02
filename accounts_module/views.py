from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts_module.serializers import UserViewSerializer, UserRegistrationSerializer


class UserRegisterView(APIView):
    """
    Register new user and response access and refresh token
    """
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserViewSerializer
    parser_classes = (MultiPartParser,)

    def get(self, request):
        """
        Get user profile information
        """
        user = request.user
        serializer = UserViewSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        """
        Update user profile information
        """
        user = request.user
        serializer = UserViewSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
