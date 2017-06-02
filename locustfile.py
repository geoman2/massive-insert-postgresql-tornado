import json

from locust import HttpLocust
from locust import TaskSet
from locust import task

class UserBehavior(TaskSet):

    @task(0)
    def post_copy(self):

        items = [{"message": "hello world"}]
        data = {"messages": items * 100}

        self.client.post(
            "/copy",
            json.dumps(data),
        )

    @task(0)
    def post_insert_transaction(self):

        items = [{"message": "hello world"}]
        data = {"messages": items * 100}

        self.client.post(
            "/insert-transaction",
            json.dumps(data),
        )

    @task(10)
    def post_multiple_inserts(self):

        items = [{"message": "hello world"}]
        data = {"messages": items * 100}

        self.client.post(
            "/multiple-inserts",
            json.dumps(data),
        )

class WebsiteUser(HttpLocust):
    task_set = UserBehavior

    min_wait = 5
    max_wait = 5
