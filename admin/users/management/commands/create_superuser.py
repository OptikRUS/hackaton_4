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
        self.stdout.write("Creating new superuser...")
        username = options['username']
        password = options['password']
        superuser = User.objects.create_superuser(
            username=username,
            password=password,
        )
        fill_supervisor_and_supervision()
        fill_counseling_themes()
        self.stdout.write(f'Суперпользователь {superuser.username} создан')
