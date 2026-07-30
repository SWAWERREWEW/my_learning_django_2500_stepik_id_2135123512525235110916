# sitewomen\women\apps.py
from django.apps import AppConfig


class WomenConfig(AppConfig):
    verbose_name = "Приложение Женщина"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'women'
