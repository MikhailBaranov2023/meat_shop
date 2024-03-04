from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            phone='your phone',
            first_name='Your first name',
            last_name='Your last name',
            city='Your city',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('your password')
        user.save()
