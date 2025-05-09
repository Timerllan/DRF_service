from django.contrib import admin
from .models import Payments, User


class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_date', 'course', 'lesson', 'payments_method', 'summ_payment')
    search_fields = ('user__username', 'course__name', 'lesson__name', 'payments_method')
    list_filter = ('payment_date', 'payments_method', 'course', 'lesson')
    list_select_related = ('user', 'course', 'lesson')  # Оптимизация запросов


admin.site.register(Payments, PaymentsAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'city', 'avatar')
    search_fields = ('email', 'phone', 'city')
    list_filter = ('email', 'city',)


admin.site.register(User, UserAdmin)
