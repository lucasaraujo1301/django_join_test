from rest_framework import viewsets

from core.models import Target
from targets import serializers


class TargetViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TargetSerializer
    queryset = Target.objects.all()
