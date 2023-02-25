from rest_framework.views import APIView
from rest_framework import status
from registration.api.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer
)
from rest_framework.response import Response
import time

# Create your views here.
class UserLoginAPIView(APIView):
    """ Users login API View """

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'status': 200,
            'user': user.username,
            'access_token': token
        }
        response = Response(data, status=status.HTTP_201_CREATED)
        response.set_cookie('access_token', token, httponly=True)
        return response
    
class UserSignUpAPIView(APIView):
    """ Users sign up API View """

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
