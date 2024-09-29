from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from users.models import User
from users.permissions import IsUserProfile
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Представление для модели User
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]