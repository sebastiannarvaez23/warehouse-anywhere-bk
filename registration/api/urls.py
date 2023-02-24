from django.urls import path
from .api import (
    UserLoginAPIView,
    UserSignUpAPIView
)

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name="login"),
    path('users/signup/', UserSignUpAPIView.as_view(), name="signup"),
]