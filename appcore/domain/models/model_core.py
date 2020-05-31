"""ModelCore module for all models in the app"""
from django.db import models

from rest_framework.utils import model_meta


class ModelCore(models.Model):
    """Base model for all models in the app"""
    create_at = models.DateTimeField(auto_now_add=True, editable=False)

    update_at = models.DateTimeField(auto_now=True, editable=False)

    fillables = []

    class Meta:
        """CoreModel class Meta"""
        abstract = True

    @property
    def is_new_instance(self):
        """
        Return if a current instance exist in database
        :return: bool
        """
        # pylint: disable = no-member
        return self.id is None

    def fill(self, attributes: {}) -> None:
        """
        Set specified values on current instance
        :param attributes: Dict
        :return: None
        """
        for attr_name in attributes:
            fillables = self.get_fillables()
            if not fillables:
                raise NotImplementedError(
                    "There is not specified any field as fillable.")

            if attr_name in fillables:
                value = attributes[attr_name]
                setattr(self, attr_name, value)

    def get_fillables(self) -> []:
        """
        Return fillable fields
        :return: []
        """
        return self.fillables

    def get_fillable_data(self) -> {}:
        """
        Return a dict with all values with keys included in fillables
        :return: {}
        """
        result = {}
        for field in self.get_fillables():
            try:
                result[field] = getattr(self, field)
            except AttributeError:
                continue

        return result

    @property
    def fields_with_relations(self) -> []:
        """
        Return a tuple with list of fields with any relation (many-to-many or
        one-to-many)
        :return: Tuple
        """

        info = model_meta.get_field_info(self)
        many_to_many = []
        one_to_many = []

        for field_name, relation_info in info.relations.items():
            if relation_info.to_many:
                if relation_info.reverse:
                    one_to_many.append(field_name)
                else:
                    many_to_many.append(field_name)

        return many_to_many, one_to_many
