"""
Test end to end django views.
"""
import json

from django.urls import reverse
import pytest


pytestmark = [
    pytest.mark.django_db,
]


def test_index_view(client):
    """Verify the index view is as expected"""
    response = client.get(reverse('main-index'))
    assert response.status_code == 200
    assert b"Hi, I'm sso-django-prototype" in response.content