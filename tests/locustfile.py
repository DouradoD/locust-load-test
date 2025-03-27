from locust import HttpUser, task, between


class UserApiUser(HttpUser):
    wait_time = between(1, 3)  # Wait between 1-3 seconds between tasks

    @task
    def create_user(self):
        self.client.post("/users", json={
            "name": "Locust User",
            "email": f"user{self.user_id}@locust.com"
        })

    @task(3)  # 3x more likely to run than create
    def get_users(self):
        self.client.get("/users")

    @task(2)
    def get_single_user(self):
        # First create a user to ensure one exists
        create_resp = self.client.post("/users", json={
            "name": "Test User",
            "email": "test@locust.com"
        })
        user_id = create_resp.json()["id"]
        self.client.get(f"/users/{user_id}")