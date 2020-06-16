"""Model class for customized account"""
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.domain.models.validators import phone_validator
from appcore.domain.models.model_core import ModelCore


class UserManager(BaseUserManager):
    """Overriding AbstractUser UserManager to exclude username field"""
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a account with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser, ModelCore):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    email and password are required. Other fields are optional.
    """

    # pylint: disable=too-few-public-methods
    class Meta:
        """CustomUser metaclass"""
        ordering = ['-id']

    username = None

    email = models.EmailField(_('email address'), unique=True,
                              blank=False,
                              validators=[EmailValidator])
    phone_number = models.CharField(_('phone number'), unique=True,
                                    max_length=20,
                                    blank=False,
                                    validators=[phone_validator],
                                    error_messages={
                                        'unique': _(
                                            "A user with that email "
                                            "already exists."),
                                    },
                                    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    fillables = ['email', 'phone_number', 'first_name', 'last_name']

    def __str__(self):
        return self.email
