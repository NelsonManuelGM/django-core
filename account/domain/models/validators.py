"""validator module"""
import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def phone_validator(string):
    """Phone validator"""
    pattern = r'^\+?(\ ?\d)+$'
    result = re.fullmatch(pattern, string)
    if not result:
        raise ValidationError(_('Incorrect phone number'),
                              params={'value': string})
    return result
