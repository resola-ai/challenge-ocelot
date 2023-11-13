import pytest
from django.urls import reverse
from pytest_lazyfixture import lazy_fixture
from rest_framework import status


@pytest.mark.parametrize(
    ["client", "expected_status"], [
        [lazy_fixture('authenticated_api_client'), status.HTTP_201_CREATED],
        [lazy_fixture('unauthenticated_api_client'), status.HTTP_401_UNAUTHORIZED],  # noqa
    ],
)
def test_create_staff(client, expected_status):
    url = reverse("staff")
    data = {
        "email": "example@example.com",
        "new_password": "1234",
    }
    response = client.post(url, data, format="json")
    assert response.status_code == expected_status
