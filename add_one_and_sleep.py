import time

import ray

ray.init(address='auto')  # Initialize Ray


@ray.remote
def add_one_and_sleep(x):
    time.sleep(1)  # Sleep for 1 second
    return x + 1  # Adds 1 to the input value


# Record the start time
start_time = time.time()

# Use a list to keep track of the futures
futures = []

# Start 5 tasks in parallel
for i in range(5):
    future = add_one_and_sleep.remote(i)
    futures.append(future)

# Get the results.
results = ray.get(futures)
print(results)  # Prints '[1, 2, 3, 4, 5]'

# Record the end time
end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
