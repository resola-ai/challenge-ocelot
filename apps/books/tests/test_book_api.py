import pytest
from django.urls import reverse_lazy
from pytest_lazyfixture import lazy_fixture
from rest_framework import status

from apps.books.constants import BookGenre
from apps.books.factories import BookFactory


@pytest.fixture
def scientific_book():
    return BookFactory(genre=BookGenre.SCIENTIFIC)


@pytest.fixture
def book_authored_by_paulo_coelho(paulo_coelho):
    return BookFactory(author=paulo_coelho)


def test_list_book(unauthenticated_api_client, book):
    url = reverse_lazy("v1:book-list")
    response = unauthenticated_api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 1
    assert response.data['results'][0]['id'] == book.id


@pytest.mark.parametrize(
    ["client", "expected_status"], [
        [lazy_fixture('authenticated_api_client'), status.HTTP_201_CREATED],
        [lazy_fixture('unauthenticated_api_client'), status.HTTP_401_UNAUTHORIZED],  # noqa
    ],
)
def test_create_book(client, expected_status):

    url = reverse_lazy("v1:book-list")
    data = {
        "author": {
            "first_name": "lorem",
            "last_name": "ipsum",
        },
        "title": "a fantastic book",
        "publish_date": "2023-11-12",
        "isbn": "11111",
        "price": None,
    }
    response = client.post(url, data, format="json")
    assert response.status_code == expected_status


@pytest.mark.parametrize(
    ["client", "expected_status"], [
        [lazy_fixture('authenticated_api_client'), status.HTTP_200_OK],
        [lazy_fixture('unauthenticated_api_client'), status.HTTP_401_UNAUTHORIZED],  # noqa
    ],
)
def test_update_book(book, client, expected_status):
    # Assuming book_id is the ID of the book to update
    url = reverse_lazy("v1:book-detail", kwargs={'pk': book.id})
    data = {
        "title": "An Updated Title",
        # Add other fields to update
    }
    response = client.put(url, data, format="json")
    assert response.status_code == expected_status


@pytest.mark.parametrize(
    ["client", "expected_status"], [
        [lazy_fixture('authenticated_api_client'), status.HTTP_204_NO_CONTENT],
        [lazy_fixture('unauthenticated_api_client'), status.HTTP_401_UNAUTHORIZED],  # noqa
    ],
)
def test_delete_book(book, client, expected_status):
    url = reverse_lazy("v1:book-detail", kwargs={'pk': book.id})
    response = client.delete(url)
    assert response.status_code == expected_status


def test_filter_book_by_author_last_or_first_name(
    authenticated_api_client,
    paulo_coelho,
    book,
    book_authored_by_paulo_coelho,
):
    url = reverse_lazy("v1:book-list")
    res = authenticated_api_client.get(
        f"{url}?author={paulo_coelho.first_name}",
    )
    assert res.status_code == status.HTTP_200_OK
    assert res.data["count"] == 1
    assert res.data["results"][0]["id"] == book_authored_by_paulo_coelho.id

    res = authenticated_api_client.get(
        f"{url}?author={paulo_coelho.last_name}",
    )
    assert res.status_code == status.HTTP_200_OK
    assert res.data["count"] == 1
    assert res.data["results"][0]["id"] == book_authored_by_paulo_coelho.id


def test_filter_book_by_genre(
    authenticated_api_client,
    scientific_book,
    book,
):
    url = reverse_lazy("v1:book-list")
    res = authenticated_api_client.get(
        f"{url}?genre={BookGenre.SCIENTIFIC}",
    )
    assert res.status_code == status.HTTP_200_OK
    assert res.data["count"] == 1
    assert res.data["results"][0]["id"] == scientific_book.id
