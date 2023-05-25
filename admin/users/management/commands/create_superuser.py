from django.core.management.base import BaseCommand
from django.db import transaction

from users.models import User


class Command(BaseCommand):
    help = 'Create superuser django'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Creating new superuser...")
        username = options['username']
        password = options['password']
        superuser = User.objects.create_superuser(
            username=username,
            password=password,
        )
        self.stdout.write(f'Суперпользователь {superuser.username} создан')
