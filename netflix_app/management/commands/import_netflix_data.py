import csv
from django.core.management.base import BaseCommand
from netflix_app.models import NetflixData

class Command(BaseCommand):
    help = 'Imports data from netflix_data.csv into NetflixData model'

    def handle(self, *args, **kwargs):
        file_path = 'netflix_project\netflix_data.csv'

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                NetflixData.objects.create(
                    title=row['title'],
                    type=row['type'],
                    country=row['country'],
                    release_year=int(row['release_year']),
                    duration=row['duration'],
                    genre=row['genre'],
                    director=row['director']
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported data'))
