"""create user service module"""
import inject
from django.contrib.auth import get_user_model

from account.domain.repository.repository import IUserRepository
from appcore.domain.services.service_core import ServiceCore


# pylint: disable=too-few-public-methods
class CreateUserService(ServiceCore):
    """Create user service"""
    @inject.autoparams()
    # pylint: disable=arguments-differ
    def execute(self, validated_data: dict,
                i_user_repository: IUserRepository) -> get_user_model():
        """
        Create user service
        :param validated_data: dict
        :param i_user_repository: IUserRepository
        :return: User
        """
        instance = get_user_model()()
        instance.fill(validated_data)

        return i_user_repository.create(instance)
