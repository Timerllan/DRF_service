from rest_framework import permissions


class IsModeratorOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Модераторы могут читать и редактировать любые объекты
        if request.user.groups.filter(name='Moderation').exists():
            return request.method in ['GET', 'PUT', 'PATCH']
        # Обычные пользователи работают только со своими объектами
        return obj.user == request.user


