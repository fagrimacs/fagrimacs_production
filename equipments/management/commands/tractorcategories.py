import csv
import os
from collections import Counter

from django.core.management import BaseCommand
from django.core.files.images import ImageFile
from django.conf import settings

from equipments.models import TractorCategory


class Command(BaseCommand):
    help = ("Prepopulate the database with initial data. "
            "Tractor category and subcategory")

    def handle(self, *args, **kwargs):
        self.stdout.write("\nPopulate dabatase with initial data.\n")
        c = Counter()
        fixtures_dir = os.path.join(settings.BASE_DIR, 'equipments/fixtures/')
        images_dir = os.path.join(fixtures_dir, 'images/tractor_category')
        datafile = fixtures_dir + 'tractorcategories.csv'

        with open(datafile, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                category, created = TractorCategory.objects.get_or_create(
                    name=row['name']
                )
                image = os.path.join(images_dir, f"{row['imagefilename']}")
                with open(image, 'rb') as image_f:
                    category.image = ImageFile(image_f,
                                               name=row['imagefilename'])
                    category.save()
                if created:
                    c['categories_created'] += 1
                else:
                    c['categories'] += 1

            self.stdout.write(
                "Categories processed=%d (created=%d)\n\n"
                % (c["categories"], c["categories_created"])
            )
