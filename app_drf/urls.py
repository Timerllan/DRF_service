from django.urls import path, include
from app_drf.apps import AppDrfConfig
from app_drf.views import CourseViewSet, LessonListCreateAPIView, LessonDeleteUpdateApiView
from .routers import routers

app_name = AppDrfConfig.name

urlpatterns = [
    path('', include(routers.urls)),
    path('lessons/', LessonListCreateAPIView.as_view(), name='lesson-create-list'),
    path('lessons/<int:pk>', LessonDeleteUpdateApiView.as_view(), name='lesson-delete-update')
]
