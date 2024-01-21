from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import Target
from targets import serializers


TARGETS_URLS = reverse("target:target-list")


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

    def test_create_target_success(self):
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
        self.assertEqual(target.is_expired(), False)

    def test_retrieve_targets(self):
        create_target()
        create_target()

        targets = Target.objects.all()
        target_serializer = serializers.TargetSerializer(targets, many=True)

        res = self.client.get(TARGETS_URLS)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, target_serializer.data)
