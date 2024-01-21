import datetime
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
        The create_target function creates a new target with the given name, latitude and longitude.
            Args:
                name (str): The name of the target to be created.
                latitude (str): The latitude of the target to be created.
                longitude (str): The longitude of the target to be created.

        :param self: Refer to the object itself, and is used in classes
        :param name: str: Specify the name of the target
        :param latitude: str: Set the latitude of the target
        :param longitude: str: Define the longitude of the target
        :param **extra_fields: Pass in any additional fields that are not explicitly defined
        :return: The target object
        :doc-author: Trelent
        """
        expiration_date = extra_fields.get("expiration_date", None)

        if expiration_date is not None:
            print(expiration_date, get_expiration_date_default())
            if expiration_date < get_expiration_date_default():
                raise ValueError("Expiration Date must be at least one day ahead.")

        target = self.model(
            name=name, latitude=latitude, longitude=longitude, **extra_fields
        )
        target.save()

        return target


class Target(CustomBaseModel):
    name = models.CharField(max_length=256)
    latitude = models.CharField(max_length=256)
    longitude = models.CharField(max_length=256)
    expiration_date = models.DateField(default=get_expiration_date_default())

    objects = CustomTargetManager()

    def is_expired(self):
        """
        The is_expired function checks to see if the expiration date of a given
            instance of the class is less than today's date. If it is, then it returns
            True, otherwise False.

        :param self: Refer to the current instance of a class
        :return: A boolean value
        :doc-author: Trelent
        """
        return self.expiration_date < datetime.datetime.now().date()
