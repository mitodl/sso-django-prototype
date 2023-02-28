"""
sso-django-prototype views
"""
from django.conf import settings
from django.shortcuts import render


def index(request):
    """
    The index view.
    """
    return render(request, "index.html")
