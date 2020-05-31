"""Repository implementation """
from appcore.infrastructure.postgres.repository_core import RepositoryCore
from account.domain.repository.repository import IUserRepository


class UserRepository(IUserRepository, RepositoryCore):
    """Abstract class for repository methods"""

    def create(self):
        """create abstract method"""
        pass

    def update(self):
        """update abstract method"""
        pass

    def delete(self):
        """delete abstract method"""
        pass

    def select(self):
        """select abstract method"""
        pass
