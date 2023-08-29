from django.shortcuts import render

from .serializers import UserSerializer, AuthTokenSerializer, ManageUserSerializer

from rest_framework import generics, mixins, permissions
from rest_framework.settings import api_settings

from rest_framework.authtoken.views import ObtainAuthToken

from django.shortcuts import redirect

from rest_framework.response import Response

from rest_framework.authtoken.models import Token


class CreateUserView(generics.CreateAPIView):
    '''NO AUTH HEADER REQD. Create a new user in the system.'''
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('http://127.0.0.1:8000/api/user/my-profile')
        return super().post(request, *args, **kwargs)


class CreateTokenView(ObtainAuthToken):
    '''NO AUTH HEADER REQD. Create token for registered users'''
    # custom serializer because we are using email instead of username
    serializer_class = AuthTokenSerializer
    # To support the browsable API feature of DRF
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('http://127.0.0.1:8000/api/user/my-profile')
        # from super function
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        is_seller = getattr(user,'is_seller')
        return Response({'token': token.key, 'is_seller': is_seller})

class ManageUserView(generics.RetrieveUpdateAPIView):
    '''AUTH HEADER REQD. View and Update details for logged in user'''
    serializer_class = ManageUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user







