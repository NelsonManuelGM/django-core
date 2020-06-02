"""Module to define actions on the database repository"""
from abc import abstractmethod

from django.contrib.auth import get_user_model


class IUserRepository:
    """Abstract class for repository methods"""

    # pylint: disable=too-few-public-methods
    class Meta:
        """IUserRepository metadata"""
        abstract = True

    @abstractmethod
    def create(self, instance: get_user_model(), **kwargs) -> \
            get_user_model():
        """
        abstract function to create user
        :param instance: User
        :param kwargs: {}
        :return: User
        """

    @abstractmethod
    def update(self):
        """update abstract method"""

    @abstractmethod
    def delete(self):
        """delete abstract method"""

    @abstractmethod
    def select(self):
        """select abstract method"""
