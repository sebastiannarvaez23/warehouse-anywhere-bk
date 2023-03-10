from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from registration.api.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer
)
from rest_framework.response import Response
import time

# Create your views here.
class UserLoginAPIView(ObtainAuthToken):
    """ Users login API View """

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""
        login_serializer = self.serializer_class(data=request.data, context={'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserLoginSerializer(user)
                if created:
                    return Response({
                        'status': 200,
                        'user': {
                            'id': user_serializer.id,
                            'username': user_serializer.username
                        },
                        'access_token': token
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Este usuario no puede iniciar sesion.'})
        return Response({'mensaje': 'Nombre de usuario o contraseña incorrectos.'}, 
                        status=status.HTTP_400_BAD_REQUEST)
    
class UserSignUpAPIView(APIView):
    """ Users sign up API View """

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
