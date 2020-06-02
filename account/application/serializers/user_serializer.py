"""User serializers module"""
import inject
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from account.domain.services.create_user import CreateUserService


class UserSerializer(ModelSerializer):
    """User serializer"""

    # pylint: disable=too-few-public-methods
    class Meta:
        """UserSerializer meta class"""
        model = get_user_model()
        fields = '__all__'

    def validate(self, attrs) -> {}:
        """
        Serializer validator
        :param attrs:
        :return: {}
        """
        return attrs

    # pylint: disable=arguments-differ
    @inject.autoparams()
    def create(self, validated_data, create_user_service: CreateUserService) -> \
            get_user_model():
        """
        Serializer user create
        :param validated_data: {}
        :param create_user_service: CreateUserService
        :return: User
        """

        return create_user_service.execute(validated_data)
