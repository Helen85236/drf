from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer, UserLimitedSerializer


class UserViewSet(viewsets.ViewSet):
    """
    CRUD mechanism for :model:`users.User` using DRF
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        if user == request.user:
            serializer = UserSerializer(user)
        else:
            serializer = UserLimitedSerializer(user)
        return Response(serializer.data)
