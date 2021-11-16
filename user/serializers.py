from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User, KycDocuments, BankRegistered


class UserSingupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'address', 'area_code', 'contact_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.get('password')
        instance = super(UserSingupSerializer, self).create(validated_data)
        instance.set_password(password)
        instance.save()
        return instance


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label="email",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password", "is_superuser", "is_staff")


class KycDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = KycDocuments
        fields = "__all__"


class BankRegisteredSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankRegistered
        fields = "__all__"
