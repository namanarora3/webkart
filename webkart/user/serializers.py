from rest_framework import serializers

from django.contrib.auth import get_user_model, authenticate

from django.contrib.auth import update_session_auth_hash

class ManageUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'email', 'password', 'number', 'name'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # create_user automatically encryptes teh password
        # password = validated_data.pop('password')
        user = get_user_model().objects.create_user(
            **validated_data
        )
        # user.set_password(password)
        # user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
            update_session_auth_hash(self.context.get('request'), user)

        return user

class UserSerializer(ManageUserSerializer):
    class Meta(ManageUserSerializer.Meta):
        fields = ManageUserSerializer.Meta.fields + ['is_seller']

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(
        write_only=True
    )
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            if not user:
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = ('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
