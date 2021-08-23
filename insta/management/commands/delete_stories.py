from django.core.management.base import BaseCommand
from ...models import Story
import datetime

class Command(BaseCommand):
    help = 'Deletes stories that are out of time(24h)'

    def handle(self, *args, **options):
        print(Story.objects.filter(created_at__lt=(datetime.datetime.now()-datetime.timedelta(days=1))).delete())

