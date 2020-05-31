"""This module contain parent class for all repository classes"""

from django.db import transaction

from appcore.domain.models.model_core import ModelCore


class RepositoryCore:
    """Class with basic method for postgre repository"""

    class Meta:
        """CoreRepository class Meta"""
        abstract = True

    @staticmethod
    @transaction.atomic
    def basic_save(instance: ModelCore, **kwargs):
        """
        Create/Update instance in database and many_2_many relations
        :param instance: ModelCore
        :return: User
        """
        # pylint: disable=dangerous-default-value

        print("return", instance)

        instance.save()

        #pylint: disable=unused-variable
        many_2_many_fields, one_to_many_fields = instance.fields_with_relations

        for related_field in many_2_many_fields:
            if related_field in kwargs:
                getattr(instance, related_field).set(kwargs[related_field],
                                                     clear=False)
        return instance

    @staticmethod
    @transaction.atomic
    def basic_save_one_2_many(instance: ModelCore, foreign_key_name: str,
                              related_field: str, **kwargs):
        """
        Basic method to save related objects (ont-to-many). Save to-many side.
        :param instance: Main instance
        :param foreign_key_name: Name of Foreign Key in to-many side
        :param related_field: Relation name
        :param kwargs: Dictionary with to-many instances
        :return: None
        """
        related_instances_saved = []
        related_instances_saved_ids = []
        if related_field in kwargs:
            for related_instance in kwargs[related_field]:
                setattr(related_instance, foreign_key_name, instance)
                related_instance.save()
                related_instances_saved_ids.append(related_instance.id)
                related_instances_saved.append(related_instance)
            include_filters = {foreign_key_name: instance.id}
            getattr(instance, related_field).filter(**include_filters).exclude(
                id__in=related_instances_saved_ids).delete()

        return related_instances_saved

    @staticmethod
    @transaction.atomic
    def basic_save_one_2_one(instance: ModelCore, related_field: str, **kwargs):
        """
        Basic method to save related objects (ont-to-one).
        :param instance: Main instance
        :param related_field: Relation name
        :param kwargs: Dictionary with to-many instances
        :return: None
        """
        if related_field in kwargs:
            related_instance = kwargs[related_field]
            setattr(instance, related_field, related_instance)
            instance.save()

        return instance
