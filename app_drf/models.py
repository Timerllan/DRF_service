from django.db import models

NULLABLE = {"blank": True, "null": True}


# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    preview = models.ImageField(upload_to='course_previews/', **NULLABLE, verbose_name='Превью')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    preview = models.ImageField(**NULLABLE, verbose_name='Превью')
    video_link = models.URLField(**NULLABLE, verbose_name='Ссылка на видео')
    course = models.ManyToManyField(Course, related_name='lessons', verbose_name='Курс')

    def __str__(self):
        return self.title
