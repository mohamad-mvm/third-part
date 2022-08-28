from django.contrib.auth.models import User
from rest_framework.test import APIClient
import pytest

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user_Authenticate(api_client):
    def do_user_authenticate(is_staff=False):
        api_client.force_authenticate(user=User(is_staff=is_staff))
    return do_user_authenticate
