from django.urls import path, include
from app_drf.apps import AppDrfConfig
from app_drf.views import CourseViewSet, LessonViewSet
from rest_framework.routers import DefaultRouter

app_name = AppDrfConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'lessons', LessonViewSet, basename='lessons')
urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls))
]
