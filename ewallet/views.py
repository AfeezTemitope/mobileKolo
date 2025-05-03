from rest_framework.response import  Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework.response import Response
from .serializers import CreateUserSerializer
from .models import User, Wallet
from rest_framework import status


class CustomUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class CustomTokenBlacklistView(TokenBlacklistView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({"message": "Successfully logged out"}, status=status.HTTP_205_RESET_CONTENT)
