from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserModelViewSet, PaymentsModelViewSet

app_name = 'users'

router = DefaultRouter()
router.register(r'users', UserModelViewSet, basename='users')  # Регистрация без префикса для использования /users/
router.register(r'payments', PaymentsModelViewSet, basename='payments')

# Указываем имя приложения
urlpatterns = router.urls
