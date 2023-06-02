from django.utils.text import gettext_lazy as _
from rest_framework import serializers, validators
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import User


class UserViewSerializer(serializers.ModelSerializer):
    """
    This model serializers is used to View user information and Edit some user information
    """
    username = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('username', 'nickname', 'avatar')



class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    This model serializers is used to Register/Update users
    """

    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        """
        Extra checking to ensure everything works well
        """
        password = validated_data.pop("password")
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        # Set default nickname and save user
        instance.nickname = instance.username
        instance.save()
        return instance


class LogOutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': _('Token is invalid or expired')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')
