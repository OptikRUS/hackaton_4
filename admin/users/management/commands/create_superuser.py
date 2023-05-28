from django.core.management.base import BaseCommand
from django.db import transaction

from users.models import User
from counseling.fixtures import fill_supervisor_and_supervision, fill_counseling_themes


class Command(BaseCommand):
    help = 'Create superuser django'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)

    @transaction.atomic
    def handle(self, *args, **options):
        if not options:
            username, password = "django", "password123"
        else:
            username, password = options['username'], options['password']
        self.stdout.write("Creating new superuser...")
        user: User = User.objects.filter(username=username)
        if not user:
            superuser: User = User.objects.create_superuser(
                username=username,
                password=password,
            )
            self.stdout.write(f'Суперпользователь {superuser.username} создан')
        else:
            self.stdout.write(f'Суперпользователь {user[0].username} уже существует')
        fill_supervisor_and_supervision()
        fill_counseling_themes()
