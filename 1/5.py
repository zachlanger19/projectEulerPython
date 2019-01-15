import numpy as np

increment = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
result = increment
divisors = list(range(1, 21))

while max(np.array([result] * 20) % divisors) != 0:
    result += increment

print(result)
