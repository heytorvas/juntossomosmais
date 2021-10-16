from django.apps import AppConfig
from scraper import get_updated_users

class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
        global users
        users = get_updated_users()