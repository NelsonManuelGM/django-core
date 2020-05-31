"""validator module"""
import re
import phonenumbers

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def phone_validator(value) -> bool:
    """
    Phone validator following the E164 standard
    :param value:
    :return: bool
    """
    pattern = r'^\+\d+$'
    result = re.fullmatch(pattern, value)
    if not result:
        raise ValidationError(_('Incorrect phone format, it should be '
                                'like E164 standard'),
                              params={'value': value})
    phone_number = phonenumbers.parse(value, None)
    if not phonenumbers.is_valid_number(phone_number):
        raise ValidationError(_('Invalid phone number!'),
                              params={'value': value})

    return True
