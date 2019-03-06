from django.core.management.base import BaseCommand
from news import scraper

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        scraper.remove()
        self.stdout.write("Remove")
        scraper.scrape()
        self.stdout.write("Scrape")