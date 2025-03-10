from rest_framework.routers import DefaultRouter
from .views import CourseViewSet

routers = DefaultRouter()
routers.register(r'courses', CourseViewSet, basename='courses')
