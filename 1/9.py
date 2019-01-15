from math import sqrt
from math import floor

for a in range(1, 500):
    for b in range(a, 500):
        c = sqrt(a * a + b * b)
        if c == floor(c):
            if a + b + c == 1000:
                print(a * b * c)
                break
