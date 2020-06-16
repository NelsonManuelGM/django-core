"""main module to configure dependency injection"""
from faker import Faker
from account.inject import user_inject_configuration
from faker_e164.providers import E164Provider


def faker_phone_provider():
    fake = Faker()
    fake.add_provider(E164Provider)
    return fake


def config_inject(binder):
    """ Configure dependency injection
    See: https://pypi.org/project/Inject/
    :param binder:
    :return: None
    """

    binder.install(user_inject_configuration)
    binder.bind(Faker, faker_phone_provider())
