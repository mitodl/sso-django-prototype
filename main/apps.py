"""
Django app
"""

from django.apps import AppConfig
from mitol.common import envs


class RootConfig(AppConfig):
    """AppConfig for this project"""

    name = "main"

    def ready(self):

        envs.validate()
