"""user view module"""
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from account.application.serializers.user_serializer import UserSerializer


# pylint: disable=too-many-ancestors
class UserView(ModelViewSet):
    """user view class"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'get']
