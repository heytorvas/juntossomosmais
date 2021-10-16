from django.apps import AppConfig
from api.scraper import get_updated_users

data = None

class UserConfig(AppConfig):
    name = 'api'

    def ready(self):
        global data
        data = get_updated_users()
