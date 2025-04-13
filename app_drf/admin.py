from django.contrib import admin

# Register your models here.


from .models import Course, Lesson

from django.contrib import admin
from .models import Course, Lesson


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Поля, которые будут отображаться в списке курсов
    search_fields = ('title',)  # Поля для поиска
    list_filter = ('title',)  # Фильтрация по полям


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_courses')  # Используем метод для отображения курсов
    search_fields = ('title', 'course__title')  # Поиск по названию урока и курса
    list_filter = ('course',)  # Фильтрация по курсам

    def get_courses(self, obj):
        return ", ".join([course.title for course in obj.course.all()])  # Получаем названия курсов

    get_courses.short_description = 'Курсы'  # Заголовок столбца в админке


# Регистрация моделей в админке
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
