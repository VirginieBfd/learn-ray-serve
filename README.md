# learn-ray-serve
Learn how to use Ray Serve

## Install

`ray[server]` is not supported yet for Mac M1 under conda, here a few steps to install it:
1. `conda env create --file env.yml`
2. `conda create learn-ray-serve`

## Get started with Ray Serve
1. `conda activate learn-ray-serve`
2. `python hello.py`

## Get started with Ray Cluster
See https://saturncloud.io/blog/getting-started-with-ray-clusters/ for more details.

1. ray up -y cluster.yml 
2. ray submit cluster.yml prime_number.py
3. ray down cluster.yml

You can also run a local ray cluster with: `python prime_number.py`
