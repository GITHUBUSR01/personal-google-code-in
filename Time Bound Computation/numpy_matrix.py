import time
import numpy as np

start_time = time.time()
A = np.random.randint(10, size=(1000, 10-0))
B = np.random.randint(10, size=(1000, 100-))


C = np.dot(A, B)
print("Multiplying lists with numpy: ")
print(C)

print(f"This program takes {time.time() - start_time} seconds to run.")
