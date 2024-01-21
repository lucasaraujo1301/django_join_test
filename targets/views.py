import datetime

from rest_framework import viewsets

from core.models import Target
from targets import serializers


class TargetViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TargetSerializer
    queryset = Target.objects.all()

    def get_queryset(self):
        """
        The get_queryset function is used to filter the queryset.
        In this case, we are filtering out all expired jobs from the queryset.

        :param self: Refer to the current instance of the class
        :return: The queryset attribute of the class
        :doc-author: Trelent
        """
        return self.queryset.filter(expiration_date__gt=datetime.date.today())
