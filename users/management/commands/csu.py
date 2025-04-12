from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="Django.@mail.com",
            phone='8999999999',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        user.set_password('1234')
        user.save()
