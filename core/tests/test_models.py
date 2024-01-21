import datetime

from django.test import TestCase

from core.models import Target
from core.utils import get_expiration_date_default


class TestModels(TestCase):
    def test_create_target(self):
        """
        The test_target_model function tests the creation of a target object.
        It creates a target object with name, latitude and longitude attributes.
        The function then asserts that the created target has the same name, latitude and longitude as those passed
         to it.

        :param self: Represent the instance of the class
        :return: A target object with the name, latitude, longitude and expiration date
        :doc-author: Trelent
        """
        name = "Testing"
        latitude = "-5.9241953"
        longitude = "-35.2115504"

        default_expiration_date = get_expiration_date_default()

        target = Target.objects.create_target(
            name=name, latitude=latitude, longitude=longitude
        )

        self.assertEqual(name, target.name)
        self.assertEqual(latitude, target.latitude)
        self.assertEqual(longitude, target.longitude)
        self.assertEqual(default_expiration_date, target.expiration_date)
        self.assertEqual(target.is_expired(), False)

    def test_create_target_with_invalid_expiration_date(self):
        """
        The test_create_target_with_invalid_expiration_date function tests the create_target function in
        the Target model.
        It creates a target with an expiration date that is yesterday's date, which should raise a ValueError exception.

        :param self: Refer to the object itself
        :return: An error message when the expiration date is less than one day ahead
        :doc-author: Trelent
        """
        yesterday = datetime.datetime.today().date() - datetime.timedelta(days=1)

        name = "Testing"
        latitude = "-5.9241953"
        longitude = "-35.2115504"

        with self.assertRaises(ValueError) as cm:
            Target.objects.create_target(
                name=name,
                latitude=latitude,
                longitude=longitude,
                expiration_date=yesterday,
            )

        exception = cm.exception
        self.assertEqual(
            str(exception), "Expiration Date must be at least one day ahead."
        )

    def test_create_target_without_name(self):
        """
        The test_create_target_without_name function tests the create_target function in the Target model.
        It checks if a ValueError is raised when no name is provided.

        :param self: Represent the instance of the class
        :return: A valueerror exception
        :doc-author: Trelent
        """
        with self.assertRaises(ValueError) as cm:
            Target.objects.create_target(
                name="",
                latitude="-5.9241953",
                longitude="-35.2115504",
            )

        exception = cm.exception
        self.assertEqual(str(exception), "Name must be provided.")

    def test_create_target_without_latitude(self):
        """
        The test_create_target_without_latitude function tests the create_target function in the Target model manager.
        It checks that a ValueError is raised if latitude is not provided.

        :param self: Represent the instance of the class
        :return: A valueerror exception
        :doc-author: Trelent
        """
        with self.assertRaises(ValueError) as cm:
            Target.objects.create_target(
                name="Teste",
                latitude="",
                longitude="-35.2115504",
            )

        exception = cm.exception
        self.assertEqual(str(exception), "Latitude must be provided.")

    def test_create_target_without_longitude(self):
        """
        The test_create_target_without_longitude function tests the create_target function in the Target model manager.
        It checks if a ValueError is raised when trying to create a target without providing longitude.

        :param self: Represent the instance of the class
        :return: A valueerror exception
        :doc-author: Trelent
        """
        with self.assertRaises(ValueError) as cm:
            Target.objects.create_target(
                name="Teste",
                latitude="-5.9241953",
                longitude="",
            )

        exception = cm.exception
        self.assertEqual(str(exception), "Longitude must be provided.")
