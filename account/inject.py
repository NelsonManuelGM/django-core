"""User inject module"""


def user_inject_configuration(binder):
    """User inject configuration function"""
    from .domain.repository.repository import IUserRepository
    from .infrastructure.postrgres.repository import UserRepository

    binder.bind(IUserRepository, UserRepository())
