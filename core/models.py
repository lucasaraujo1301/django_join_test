import uuid

from django.db import models

from core.utils import get_expiration_date_default


class CustomBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class CustomTargetManager(models.Manager):
    def create_target(self, name: str, latitude: str, longitude: str, **extra_fields):
        """
        The create_target function creates a new target with the given name, latitude, and longitude.
            The function also accepts an expiration_date argument which is optional. If no expiration date is provided,
            then the default value of one day from now will be used.

        :param self: Refer to the object itself
        :param name: str: Ensure that the name of the target is provided
        :param latitude: str: Ensure that the latitude is a string
        :param longitude: str: Specify the longitude of a target
        :param **extra_fields: Pass in the expiration_date field
        :return: A target object
        :doc-author: Trelent
        """
        if not name:
            raise ValueError("Name must be provided.")
        if not latitude:
            raise ValueError("Latitude must be provided.")
        if not longitude:
            raise ValueError("Longitude must be provided.")

        expiration_date = extra_fields.get("expiration_date", None)

        if expiration_date is not None:
            if expiration_date < get_expiration_date_default():
                raise ValueError("Expiration Date must be at least one day ahead.")

        return self.create(
            name=name, latitude=latitude, longitude=longitude, **extra_fields
        )


class Target(CustomBaseModel):
    name = models.CharField(max_length=256)
    latitude = models.CharField(max_length=256)
    longitude = models.CharField(max_length=256)
    expiration_date = models.DateField(default=get_expiration_date_default())

    objects = CustomTargetManager()
