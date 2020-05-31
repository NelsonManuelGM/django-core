"""main module to configure dependency injection"""
from faker import Faker
from account.inject import user_inject_configuration


def config_inject(binder):
    """ Configure dependency injection
    See: https://pypi.org/project/Inject/
    :param binder:
    :return: None
    """

    binder.install(user_inject_configuration)
    binder.bind(Faker, Faker(['en_US', 'es_ES']))
