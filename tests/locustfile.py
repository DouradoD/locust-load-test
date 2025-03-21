from locust import HttpUser, task, between
from api.services.post_service import PostService
from data.test_data import TestData

class ApiUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        self.post_service = PostService(self.client)

    @task
    def get_posts(self):
        self.post_service.get_posts()

    @task(3)
    def create_post(self):
        self.post_service.create_post(TestData.POST_DATA)