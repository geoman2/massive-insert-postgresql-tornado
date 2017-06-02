from locust import HttpLocust
from locust import TaskSet
from locust import task

class UserBehavior(TaskSet):

    @task(10)
    def ping(self):
        self.client.post("/copy")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior

    min_wait = 5
    max_wait = 5
