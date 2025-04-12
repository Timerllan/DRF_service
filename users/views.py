from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from users.models import User, Payments
from users.serializer import UserSerializer, PaymentsSerializer


# Create your views here.


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentsModelViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['payment_date']
    filterset_fields = ('lesson', 'course', 'payments_method')


# Задание 4
# Настройте фильтрацию для эндпоинтов вывода списка платежей с возможностями:
#
# менять порядок сортировки по дате оплаты,
# фильтровать по курсу или уроку,
# фильтровать по способу оплаты.
