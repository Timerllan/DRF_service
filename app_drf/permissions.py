from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        # Разрешаем только просмотр и изменение объектов
        if request.method in permissions.SAFE_METHODS:
            return True  # Разрешаем просмотр
        if request.method in ['PUT', 'PATCH']:
            return request.user.groups.filter(name='moderators').exists()  # Разрешаем изменение для модераторов
        return False



