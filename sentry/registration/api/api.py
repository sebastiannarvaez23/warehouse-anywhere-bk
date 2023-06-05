import time

from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from sentry.company.models import Company, Domain
from sentry.registration.api.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer
)

# Create your views here.


class UserLoginAPIView(APIView):
    """ Users login API View """

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        user_company = Company.objects.get(user=user)
        user_domain_company = Domain.objects.get(id=user_company.id)
        data = {
            'status': 200,
            'user': {
                'id': user.id,
                'username': user.username,
                'domain': user_domain_company.domain
            },
            'access_token': token
        }
        response = Response(data, status=status.HTTP_200_OK)
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
