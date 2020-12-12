import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")

    @task(3)
    def view_item(self):
        for random in range(10):
            self.client.get(f"/sentence/{random}", name="/sentence")
            time.sleep(1)

