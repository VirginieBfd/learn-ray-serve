import os
from random import random

import ray
from ray import serve

serve.start()


class Model:
    def __init__(self, path):
        self.path = path

    def predict(self, data):
        return random() + data if data > 0.5 else data


@serve.deployment
class Deployment:
    def __init__(self, path: str):
        self.path = path
        self.model = Model(path)
        self.pid = os.getpid()

    def predict(self, data):
        pred = self.model.predict(float(data))
        return f"(pid: {self.pid}); path: {self.path}; data: {float(data): .3f}; prediction: {pred: .3f}"

    def __call__(self, starlette_request):
        return self.predict(starlette_request.query_params["data"])


Deployment.options(name="rep-1", num_replicas=2).deploy("/model/rep-1.pkl")
Deployment.options(name="rep-2", num_replicas=2).deploy("/model/rep-2.pkl")

print(serve.list_deployments())

for _ in range(2):
    for d_name in ["rep-1", "rep-2"]:
        handle = serve.get_deployment(d_name).get_handle()
        print(f"handle name {d_name}")
        print(f"prediction: {ray.get(handle.predict.remote(random()))}")

serve.shutdown()
