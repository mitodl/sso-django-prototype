"""
Test end to end django views.
"""

from django.urls import reverse
import pytest


pytestmark = [
    pytest.mark.django_db,
]


def test_index_view(client):
    """Verify the index view is as expected"""
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert b"Login" in response.content
