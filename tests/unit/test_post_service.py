import pytest
from tests.api.services.post_service import PostService
from tests.data.test_data import TestData

@pytest.fixture
def post_service():
    return PostService("https://jsonplaceholder.typicode.com")

def test_get_posts(post_service):
    response = post_service.get_posts()
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_post(post_service):
    response = post_service.create_post(TestData.POST_DATA)
    assert response.status_code == 201
    assert response.json()["title"] == TestData.POST_DATA["title"]