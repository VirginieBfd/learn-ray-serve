# learn-ray-serve
Learn how to use Ray Serve

## Install

`ray[server]` is not supported yet for Mac M1 under conda, here a few steps to install it:
1. `conda env create --file env.yml`
2. `conda create learn-ray-serve`

## Get started
1. Run locally with `serve run hello:graph`
2. Ping from other local terminal `curl -X PUT "http://localhost:8000/?name=Ray"`