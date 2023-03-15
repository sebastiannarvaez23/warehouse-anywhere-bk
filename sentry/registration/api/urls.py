from django.urls import path
from .api import (
    UserLoginAPIView,
    UserSignUpAPIView
)

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name="login"),
    path('signup/', UserSignUpAPIView.as_view(), name="signup"),
]