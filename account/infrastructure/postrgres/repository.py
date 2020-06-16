"""Repository implementation """
from django.contrib.auth import get_user_model

from account.domain.repository.repository import IUserRepository
from appcore.infrastructure.postgres.repository_core import RepositoryCore


class UserRepository(IUserRepository, RepositoryCore):
    """Abstract class for repository methods"""

    def create(self, instance: get_user_model(), **kwargs) -> \
            get_user_model():
        """
        function to create user
        :param instance: User
        :param kwargs: {}
        :return: User
        """

        return self.basic_save(instance)

    def update(self):
        """update abstract method"""

    def delete(self):
        """delete abstract method"""

    def select(self):
        """select abstract method"""
