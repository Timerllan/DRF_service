from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Course, Lesson
from .serializer import CourseSerializer, LessonSerializer
from rest_framework import viewsets, status


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDeleteUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
