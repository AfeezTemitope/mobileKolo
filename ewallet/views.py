from rest_framework.viewsets import ModelViewSet
from .serializers import CreateUserSerializer
from .models import User, Wallet


class CustomUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


