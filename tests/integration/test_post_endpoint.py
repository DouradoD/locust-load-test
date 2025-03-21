import pytest
from tests.api.endpoints.post_endpoint import PostEndpoint
from tests.data.test_data import TestData

@pytest.fixture
def post_endpoint():
    return PostEndpoint("https://jsonplaceholder.typicode.com")

def test_get_all_posts(post_endpoint):
    response = post_endpoint.get_all()
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_post(post_endpoint):
    response = post_endpoint.create(TestData.POST_DATA)
    assert response.status_code == 201
    assert response.json()["title"] == TestData.POST_DATA["title"]