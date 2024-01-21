from rest_framework import serializers

from core.models import Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ["id", "name", "latitude", "longitude", "expiration_date"]
        read_only_fields = ["id"]

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
