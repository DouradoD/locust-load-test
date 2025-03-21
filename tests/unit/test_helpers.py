import pytest
from tests.utils.helpers import Utils

def test_validate_response():
    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code

    response = MockResponse(200)
    Utils.validate_response(response, 200)

    with pytest.raises(AssertionError):
        Utils.validate_response(response, 404)