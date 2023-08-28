from django.shortcuts import render

from .serializers import UserSerializer, AuthTokenSerializer, ManageUserSerializer

from rest_framework import generics, mixins, permissions
from rest_framework.settings import api_settings

from rest_framework.authtoken.views import ObtainAuthToken

from django.shortcuts import redirect


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
        return super().post(request, *args, **kwargs)

class ManageUserView(generics.RetrieveUpdateAPIView):
    '''AUTH HEADER REQD. View and Update details for logged in user'''
    serializer_class = ManageUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user







