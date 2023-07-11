from rest_framework import serializers
from information.models import Information


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ['id', 'title', 'section', 'details', 'status']
