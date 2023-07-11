from rest_framework import viewsets
from information.models import Information
from information.serializers import InformationSerializer


class InfoViewSet(viewsets.ModelViewSet):
    serializer_class = InformationSerializer
    queryset = Information.objects.all()

