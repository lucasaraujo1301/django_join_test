from rest_framework import serializers

from core.models import Target
from core.utils import get_expiration_date_default


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ["id", "name", "latitude", "longitude", "expiration_date"]
        read_only_fields = ["id"]

    def validate_expiration_date(self, value):
        """
        The validate_expiration_date function is a custom validation function that checks if the expiration date
            of an item is at least one day ahead. If it isn't, then the serializer will raise a ValidationError.

        :param self: Access the object that is being validated
        :param value: Pass the value of the field to be validated
        :return: The value if it is not none and the value is greater than one day ahead
        :doc-author: Trelent
        """
        if value is not None:
            if value < get_expiration_date_default():
                raise serializers.ValidationError(
                    "Expiration Date must be at least one day ahead."
                )
        return value

    def create(self, validated_data):
        """
        The create function is used to create a new instance of the model when
        POSTing to an endpoint that represents a collection of objects. The validated_data
        argument contains all the fields in your serializer, valid and ready to be saved.
        The create function should return the created object instance.

        :param self: Represent the instance of the class
        :param validated_data: Pass the data from the serializer to the model
        :return: The instance of the model created
        :doc-author: Trelent
        """
        return Target.objects.create_target(**validated_data)
