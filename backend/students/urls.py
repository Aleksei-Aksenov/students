from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import StudentsViewSet

router = DefaultRouter()
router.register('students', StudentsViewSet)

urlpatterns = router.urls
