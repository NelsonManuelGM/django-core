"""Base module for system services"""
from abc import abstractmethod

from appcore.domain.models.model_core import ModelCore


# pylint: disable=too-few-public-methods
class ServiceCore:
    """Base service for app services"""

    # pylint: disable=too-few-public-methods
    class Meta:
        """Service core metaclass"""
        abstract = True

    @abstractmethod
    def execute(self, validate_data: dict) -> ModelCore:
        """execute service function"""
