"""TestCore configuration"""
import inject
from django.test import TestCase
from faker import Faker
from rest_framework.test import APITestCase, APIClient

from djcore.inject import config_inject


class TestCaseCore(TestCase):
    """Parent class for system tests"""

    # pylint: disable=too-few-public-methods
    class Meta:
        """meta class"""
        abstract = True

    def setUp(self) -> None:
        super().setUp()
        inject.clear_and_configure(config_inject)


class APITestCaseCore(APITestCase, TestCase):
    """Parent class for system tests"""

    # pylint: disable=too-few-public-methods
    class Meta:
        """meta class"""
        abstract = True

    def setUp(self) -> None:
        inject.clear_and_configure(config_inject)
        self.client = APIClient()

    @staticmethod
    @inject.autoparams()
    def generate_fake_user_dict(faker: Faker) -> dict:
        """create fake user function"""
        first_name = faker.last_name()
        return {
            'first_name': first_name,
            'last_name': faker.last_name(),
            'password': first_name,
            'email': faker.email(),
            'phone_number': faker.e164(),
            'address': faker.address(),
        }
