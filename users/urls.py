from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserModelViewSet

app_name = 'users'
# Создаем роутер
router = DefaultRouter()
router.register(r'', UserModelViewSet, basename='users')  # Регистрация без префикса для использования /users/

# Указываем имя приложения
urlpatterns = router.urls
