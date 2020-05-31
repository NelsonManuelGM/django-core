import inject
from django.core.exceptions import ValidationError
from faker import Faker

from account.domain.models.validators import phone_validator
from appcore.tests.test_core import TestCaseCore


class CreateUserTest(TestCaseCore):

    def setUp(self) -> None:
        super().setUp()

    def test_validator_for_wrong_phone_number(self):
        phone = "+1-525-300-522-321"
        with self.assertRaises(ValidationError):
            phone_validator(phone)

    @inject.autoparams()
    def test_validator_for_write_phone_number(
            self, faker: Faker):
        phone = faker.phone_number()
        result = phone_validator(phone)
        self.assertEqual(result.string, phone)
