import random

class Utils:
    @staticmethod
    def validate_response(response, expected_status_code):
        assert response.status_code == expected_status_code, f"Expected {expected_status_code}, got {response.status_code}"

    @staticmethod
    def generate_random_email():
        return f"user_{random.randint(1, 1000)}@example.com"