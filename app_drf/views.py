from .models import Course, Lesson
from .serializer import CourseSerializer, LessonSerializer
from rest_framework import viewsets
from app_drf.permissions import IsModeratorOrOwner


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsModeratorOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Moderation').exists():
            return Course.objects.all()  # Модераторы видят ВСЁ
        return Course.objects.filter(user=user)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModeratorOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Moderation').exists():
            return Lesson.objects.all()  # Модераторы видят ВСЁ
        return Lesson.objects.filter(user=user)