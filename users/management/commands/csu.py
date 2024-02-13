from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            phone='9998502717',
            first_name='Mikhail',
            last_name='Baranov',
            city='Porto',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('1qazxsw23edc')
        user.save()
