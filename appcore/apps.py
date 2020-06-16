"""AppCore configuration"""
from django.apps import AppConfig


class AppCoreConfig(AppConfig):
    """AppCore configuration"""
    name = 'appcore'

    class Meta:
        """AppCore metaclass"""
        abstract = True
