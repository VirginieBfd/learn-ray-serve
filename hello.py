import starlette.requests
from ray import serve


@serve.deployment
class Doubler:
    def double(self, s: str):
        return s + " " + s


@serve.deployment
class HelloDeployment:
    def __init__(self, doubler):
        self.doubler = doubler

    async def say_hello_twice(self, name: str):
        ref = await self.doubler.double.remote(f"Hello, {name}!")
        return await ref

    async def __call__(self, request: starlette.requests.Request):
        return await self.say_hello_twice(request.query_params["name"])


graph = HelloDeployment.bind(Doubler.bind())
