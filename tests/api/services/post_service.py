import requests

class PostService:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_posts(self):
        response = requests.get(f"{self.base_url}/posts")
        return response

    def create_post(self, data):
        response = requests.post(f"{self.base_url}/posts", json=data)
        return response