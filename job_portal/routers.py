from rest_framework.routers import DefaultRouter
from information.viewsets import InfoViewSet
from jobs.viewsets import JobViewSet


router = DefaultRouter()
router.register('info', InfoViewSet)
router.register('jobs', JobViewSet)
