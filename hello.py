import requests
from ray import serve

serve.start()


@serve.deployment
def hello(request):
    name = request.query_params["name"]
    return f"Hello {name}"


hello.deploy()

import requests

for i in range(10):
    response = requests.get(f"http://127.0.0.1:8000/hello?name={i}").text
    print(f"{i}: {response}")

serve.shutdown()
