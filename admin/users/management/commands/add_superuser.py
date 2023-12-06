import os

from pathlib import Path
from dotenv import load_dotenv

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


class Command(BaseCommand):
    def handle(self, *args, **options):
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        if not User.objects.filter(username=username).exists():
            admin = User.objects.create_superuser(username=username, password=password)
            print(f"Аккаунт создан {admin}")
        else:
            print("Такой аккаунт уже существует.")
