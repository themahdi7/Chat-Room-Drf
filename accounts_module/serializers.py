from rest_framework import serializers, validators
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
