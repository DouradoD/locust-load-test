import requests

class PostEndpoint:
    def __init__(self, base_url):
        self.base_url = f"{base_url}/posts"

    def get_all(self):
        return requests.get(self.base_url)

    def get_by_id(self, post_id):
        return requests.get(f"{self.base_url}/{post_id}")

    def create(self, data):
        return requests.post(self.base_url, json=data)