from django.apps import AppConfig

from .utils import delete_files_in_downloads_folder


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        delete_files_in_downloads_folder()
