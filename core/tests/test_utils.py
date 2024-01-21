import datetime

from django.test import SimpleTestCase

from core.utils import get_expiration_date_default


class TestUtils(SimpleTestCase):
    def test_get_expiration_date_default(self):
        """
        The test_get_expiration_date_default function tests the get_expiration_date_default function.
        The test asserts that the default expiration date is two days from now.

        :param self: Represent the instance of the class
        :return: The date two days from today
        :doc-author: Trelent
        """
        default_date = get_expiration_date_default()

        after_tomorrow_date = datetime.datetime.now().date() + datetime.timedelta(
            days=1
        )

        self.assertEqual(after_tomorrow_date, default_date)
