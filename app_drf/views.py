from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Course, Lesson
from .serializer import CourseSerializer, LessonSerializer
from rest_framework import viewsets, status


# Create your views here.

class CourseViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # 5. Если данные не valid, возвращаем ошибки
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        list_object = Course.objects.all()
        serializer = CourseSerializer(list_object, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            obj = Course.objects.get(pk=pk)
            serializer = CourseSerializer(obj)
            return Response(serializer.data)
        except Course.DoesNotExist:
            return Response(
                {"detail": "Course not found."},
                status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk=None):
        try:
            obj = Course.objects.get(pk=pk)
            serializer = CourseSerializer(obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)  # Возвращаем обновленные данные
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Обработка ошибок
        except Course.DoesNotExist:
            return Response(
                {"detail": "Course not found."},
                status=status.HTTP_404_NOT_FOUND
            )

    def destroy(self, request, pk=None):
        try:
            # Получаем объект по первичному ключу (pk)
            obj = Course.objects.get(pk=pk)
            obj.delete()  # Удаляем объект
            return Response(status=status.HTTP_204_NO_CONTENT)  # Возвращаем 204 No Content
        except Course.DoesNotExist:
            return Response(
                {"detail": "Course not found."},
                status=status.HTTP_404_NOT_FOUND
            )


class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDeleteUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
