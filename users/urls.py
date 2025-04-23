from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserModelViewSet, PaymentsModelViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'users'

router = DefaultRouter()
router.register(r'users', UserModelViewSet, basename='users')  # Регистрация без префикса для использования /users/
router.register(r'payments', PaymentsModelViewSet, basename='payments')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),  # Включаем маршруты из роутера
]
