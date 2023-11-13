import pytest
from django.urls import reverse_lazy
from pytest_lazyfixture import lazy_fixture
from rest_framework import status


def test_list_book(unauthenticated_api_client, book):
    url = reverse_lazy("book-list")
    response = unauthenticated_api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 1
    assert response.data['results'][0]['id'] == book.id


@pytest.mark.parametrize("client, expected_status", [
    (lazy_fixture('authenticated_api_client'), status.HTTP_201_CREATED),
    (lazy_fixture('unauthenticated_api_client'), status.HTTP_401_UNAUTHORIZED)  # Assuming unauthenticated should get a 403
])
def test_create_book(client, expected_status):

    url = reverse_lazy("book-list")
    data = {
        "author": {
            "first_name": "lorem",
            "last_name": "ipsum"
        },
        "title": "a fantastic book",
        "publish_date": "2023-11-12",
        "isbn": "11111",
        "price": None
    }
    response = client.post(url, data, format="json")
    assert response.status_code == expected_status


@pytest.mark.parametrize("client, expected_status", [
    (lazy_fixture('authenticated_api_client'), status.HTTP_200_OK),  # Assuming authenticated can update
    (lazy_fixture('unauthenticated_api_client'), status.HTTP_401_UNAUTHORIZED)  # Assuming unauthenticated should get a 401
])
def test_update_book(book, client, expected_status):
    # Assuming book_id is the ID of the book to update
    book_id = 1  # Update with the appropriate book ID
    url = reverse_lazy("book-detail", kwargs={'pk': book.id})
    data = {
        "title": "An Updated Title"
        # Add other fields to update
    }
    response = client.put(url, data, format="json")
    assert response.status_code == expected_status

@pytest.mark.parametrize("client, expected_status", [
    (lazy_fixture('authenticated_api_client'), status.HTTP_204_NO_CONTENT),  # Assuming authenticated can delete
    (lazy_fixture('unauthenticated_api_client'), status.HTTP_401_UNAUTHORIZED)  # Assuming unauthenticated should get a 401
])
def test_delete_book(book, client, expected_status):
    # Assuming book_id is the ID of the book to delete
    book_id = 1  # Delete the appropriate book ID
    url = reverse_lazy("book-detail", kwargs={'pk': book.id})
    response = client.delete(url)
    assert response.status_code == expected_status
