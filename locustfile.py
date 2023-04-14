from locust import HttpUser, task, between
from random import randint

class LoadTester(HttpUser):
    @task(3)
    def new_user(self):
        self.client.get("/categories")
        self.client.get("/products")
        amount_items = randint(0,5)

        for i in range(amount_items):
            item = randint(1,80)
            self.client.get(f"/products/{item}")
    
    @task(2)
    def existing_user(self):
        user = randint(1,20)
        self.client.get(f"/customers/{user}")
        self.client.get("/products")
        
        amount_cat = randint(0,3)
        for i in range(amount_cat):
            cat = randint(1,6)
            self.client.get(f"/categories/{cat}")


        amount_items = randint(0,15)

        for i in range(amount_items):
            item = randint(1,80)
            self.client.get(f"/products/{item}")


