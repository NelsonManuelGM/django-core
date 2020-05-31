"""module for phone validator testing"""
import inject
from django.core.exceptions import ValidationError
from faker import Faker

from account.domain.models.validators import phone_validator
from appcore.tests.test_core import TestCaseCore


class PhoneValidatorTest(TestCaseCore):
    """Code to test phone validator using the E164 standard"""

    @inject.autoparams()
    def test_validator_for_wrong_number_structure(self, faker: Faker):
        """
        :param faker: Faker
        :return:
        """
        value = faker.phone_number()
        with self.assertRaises(ValidationError) as ex:
            phone_validator(value)
        self.assertEqual(ex.exception.message,
                         'Incorrect phone format, '
                         'it should be like E164 standard')

    @inject.autoparams()
    def test_validator_for_wrong_phone_number(self, faker: Faker):
        """
        :param faker: Faker
        :return:
        """
        value = faker.e164(valid=False)
        with self.assertRaises(ValidationError) as ex:
            phone_validator(value)
        self.assertEqual(ex.exception.message, 'Invalid phone number!')

    @inject.autoparams()
    def test_validator_for_write_phone_number(self, faker: Faker):
        """
        :param faker: Faker
        :return:
        """
        value = faker.e164()
        result = phone_validator(value)
        self.assertEqual(result, True)
