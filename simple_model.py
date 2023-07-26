from random import random

import requests
from ray import serve

serve.start()


@serve.deployment
class SimpleModel:
    def __init__(self):
        self.weight = 0.5
        self.bias = 1
        self.prediction = 0

    def predict(self, data):
        self.prediction = float(data) * self.weight * random() + self.bias
        return {"prediction": self.prediction}

    def __call__(self, starlette_request):
        return self.predict(starlette_request.query_params["data"])


SimpleModel.deploy()

url = "http://127.0.0.1:8000/SimpleModel"
for i in range(5):
    response = requests.get(url, params={"data": random()}).text
    print(f"{i}: {response}")

print(serve.list_deployments())

serve.shutdown()
