import datetime

from django.test import TestCase
from django.urls import reverse
from freezegun import freeze_time
from rest_framework.test import APIClient
from rest_framework import status

from core.models import Target
from targets import serializers

TARGETS_URLS = reverse("target:target-list")


def custom_today():
    """
    The custom_today function is used to set the default value of the date field in
    the form.  The default value is 5 days from today's date.

    :return: A datetime object that is 5 days in the future
    :doc-author: Trelent
    """
    return datetime.date.today() + datetime.timedelta(days=5)


def detail_url(target_id):
    """
    The detail_url function is a helper function that returns the URL for an individual target.
    It takes in one argument, which is the ID of the target to be displayed.

    :param target_id: Get the target from the database
    :return: The url for the target detail page
    :doc-author: Trelent
    """
    return reverse("target:target-detail", args=[target_id])


def create_target(**params):
    """
    The create_target function creates a target object with the given parameters.


    :param **params: Receive a dictionary of parameters
    :return: A target object
    :doc-author: Trelent
    """
    default = {"name": "Test", "latitude": "-5.9241953", "longitude": "-35.2115504"}
    default.update(**params)
    return Target.objects.create_target(**default)


class TestTargetsApi(TestCase):
    def setUp(self):
        """
        The setUp function is a special function that gets run before each test.
        It's used to set up any state specific to the execution of the given test case.
        In this case, we're using it to create an APIClient instance, which will be used for making API requests.

        :param self: Represent the instance of the class
        :return: The client
        :doc-author: Trelent
        """
        self.client = APIClient()
        self.today = datetime.datetime.now().date()

    def test_create_target_success(self):
        """
        The test_create_target_success function tests the creation of a target.
        It does so by creating a payload with the necessary data to create a target, and then it sends that payload to
         the API endpoint for creating targets.
        The test asserts that:
            - The status code returned is 201 (CREATED)
            - A Target object was created in the database with all of its fields correctly set

        :param self: Represent the instance of the class
        :return: The status code 201, which means that the target was created successfully
        :doc-author: Trelent
        """
        payload = {"name": "Test", "latitude": "-5.9241953", "longitude": "-35.2115504"}

        res = self.client.post(TARGETS_URLS, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        target = Target.objects.get(
            name=payload["name"],
            latitude=payload["latitude"],
            longitude=payload["longitude"],
        )
        self.assertIsNotNone(target)
        self.assertEqual(target.name, payload["name"])

    def test_retrieve_targets(self):
        """
        The test_retrieve_targets function is a test that checks if the GET request to the /targets/ endpoint returns
        a 200 status code and a list of all targets in the database. The function first creates two target objects using
        the create_target helper function, then it retrieves all targets from the database and serializes them into JSON
         format.
        The client then makes a GET request to /targets/, which should return an HTTP 200 OK response with data equal to
        the serialized target data.

        :param self: Represent the instance of the class
        :return: The status code 200 and the data from the target_serializer
        :doc-author: Trelent
        """
        create_target()
        create_target()

        targets = Target.objects.all()
        target_serializer = serializers.TargetSerializer(targets, many=True)

        res = self.client.get(TARGETS_URLS)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, target_serializer.data)

    def test_retrieve_targets_that_is_not_expired(self):
        """
        The test_retrieve_targets_that_is_not_expired function tests the retrieve_targets_that_is_not_expired function.
        The test creates two expired targets and one non-expired target, then retrieves all non-expired targets.


        :param self: Refer to the class itself
        :return: The status code 200 and the data of the serializer
        :doc-author: Trelent
        """
        create_target()
        create_target()

        with freeze_time(custom_today()):
            create_target()

            res = self.client.get(TARGETS_URLS)

            targets_not_expired = Target.objects.filter(
                expiration_date__gt=datetime.date.today()
            )
            target_serializer = serializers.TargetSerializer(
                targets_not_expired, many=True
            )

            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(res.data, target_serializer.data)

    def test_retrieve_one_target(self):
        target = create_target()

        res = self.client.get(detail_url(target.id))

        target_serializer = serializers.TargetSerializer(target)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, target_serializer.data)

    def test_delete_target(self):
        """
        The test_delete_target function tests the DELETE method on a target.
        It creates a new target, then uses the client to send a DELETE request to /api/targets/{id}/.
        The test checks that the response has status code 204 NO CONTENT and that there are no targets with this id in
         the database.

        :param self: Represent the instance of the class
        :return: A status code of 204, which means that the request was successful and there is no content to return
        :doc-author: Trelent
        """
        target = create_target()

        res = self.client.delete(detail_url(target.id))

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        target = Target.objects.filter(pk=target.id).exists()
        self.assertFalse(target)
