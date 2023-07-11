from rest_framework import viewsets, permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS
from jobs.models import Job
from jobs.serializers import JobSerializer


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class JobViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated|ReadOnly, )
    serializer_class = JobSerializer
    queryset = Job.objects.all()
