# pip3.12 install PyThreadKiller
# Example:

import time
from PyThreadKiller import PyThreadKiller

def example_target():
    for i in range(5):
        print(f"Thread is running... {i}")
        time.sleep(1)
    return True

# Create an instance of PyThreadKiller
thread = PyThreadKiller(target=example_target)
thread.start()

# Allow the thread to run for 3 seconds
time.sleep(3)

# Kill the thread
result = thread.kill()
print(f"Return value after killing the thread: {result}")
