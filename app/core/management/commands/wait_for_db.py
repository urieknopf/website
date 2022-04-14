import time
from psycopg2 import OperationalError as Psychopg20pError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for database on startup"""

    def handle(self, *args, **options):
        """Entrypoinmt for command"""
        # self.stdout.write('Waiting for database...')  # Commented out to limit unneeded outputs
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psychopg20pError, OperationalError):
                self.wait = 1
                self.stdout.write(f'Waiting for database...')
                time.sleep(self.wait)
        
        self.stdout.write(self.style.SUCCESS('Database ready.'))