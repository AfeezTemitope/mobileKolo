from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from ewallet.views import CustomUserViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('register', CustomUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]

