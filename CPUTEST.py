import numpy as np
import time

def numpy_stress(N, duration_sec):
    print(f"Running NumPy stress test with {N}x{N} matrices for {duration_sec} seconds...")
    end_time = time.time() + duration_sec
    count = 0
    while time.time() < end_time:
        A = np.random.rand(N, N)
        B = np.random.rand(N, N)
        _ = np.dot(A, B)
        count += 1
    print(f"Matrix multiplications completed: {count}")

numpy_stress(500, 10)  # 500x500 행렬 곱을 10초간 반복
