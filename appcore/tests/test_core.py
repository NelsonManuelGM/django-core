"""TestCore configuration"""
import inject
from django.test import TestCase
from rest_framework.test import APITestCase, APIClient

from djcore.inject import config_inject


class TestCaseCore(TestCase):
    """Parent class for system tests"""

    class Meta:
        abstract = True

    def setUp(self) -> None:
        super().setUp()
        inject.clear_and_configure(config_inject)


class APITestCaseCore(APITestCase, TestCase):
    """Parent class for system tests"""
    class Meta:
        abstract = True

    def setUp(self) -> None:
        inject.clear_and_configure(config_inject)
        self.client = APIClient()
